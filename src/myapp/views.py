from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import get_user_model, login, logout
from .forms import UserLoginForm

User = get_user_model()


def check_user(request):
    # Not a view
    if not request.user.is_authenticated():
        raise Http404


def user_logout_view(request):
    check_user(request)
    logout(request)
    return HttpResponseRedirect('/')


def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    if form and form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("/")

    context = {
        'form': form,
    }

    return render(request, "user_login.html", context)


def profile_view(request, username):
    user_qs = User.objects.filter(username__iexact=username)

    if not user_qs.exists() and user_qs.count() != 1:
        raise Http404

    user_obj = user_qs.first()
    posts = Post.objects.filter(user=user_obj)
    context = {
        'user_obj': user_obj,
        'posts': posts
    }
    return render(request, 'profile_view.html', context)


def post_delete_view(request, pk=None):
    check_user(request)
    post_obj = get_object_or_404(Post, pk=pk)
    context = {
        'post': post_obj,
    }

    if request.method == 'POST':
        post_obj.delete()
        return HttpResponseRedirect('/post')
    return render(request, 'post_delete_confirm.html', context)


def post_edit_view(request, pk=None):
    check_user(request)
    post_obj = get_object_or_404(Post, pk=pk)
    form = PostModelForm(request.POST or None, instance=post_obj)

    context = {
        'post': post_obj,
        'form': form,
    }

    if request.method == 'POST':
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/post/{pk}'.format(pk=obj.pk))

    return render(request, 'post_edit.html', context)


def post_list_view(request):
    if request.method == 'POST':
        squery = request.POST['qry']
        all_posts = Post.objects.filter(
            Q(post_status='post') &
            Q(title__icontains=squery)).order_by('-create_date')

    else:
        all_posts = Post.objects.filter(post_status='post').order_by('-create_date')
        squery = None

    conetext = {
        'posts': all_posts,
        'squery': squery,
    }
    return render(request, 'post_list.html', conetext)


def post_draft_list_view(request):
    check_user(request)
    post_objs = Post.objects.filter(post_status='draft')

    context = {
        'posts': post_objs,
        'post_status': 'Draft',
    }

    return render(request, 'post_list.html', context)


def post_create_view(request):
    check_user(request)
    form = PostModelForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/post/{pk}'.format(pk=obj.pk))

    return render(request, 'post_create.html', context)


def post_list_view_tag(request, post_tag):
    post_objs = Post.objects.filter(
        Q(tag__iexact=post_tag) &
        Q(post_status='post')
    ).distinct()

    context = {
        'posts': post_objs,
        'tag': post_tag
    }
    return render(request, 'post_list.html', context)


def post_detail_view(request, pk=None):
    try:
        post = Post.objects.get(pk=pk)

    except:
        raise Http404

    if str(post.post_status) == "draft":
        post_draft = True
    else:
        post_draft = False

    context = {
        'post_obj': post,
        'is_draft': post_draft,
    }
    return render(request, 'post_detail.html', context)


def add_comment(request, pk):
    form = CommentModelForm(request.POST or None)
    post_obj = get_object_or_404(Post, pk=pk)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.post = post_obj

        if request.user.is_authenticated() and request.user == post_obj.user:
            obj.byadmin = True

        obj.save()

        return HttpResponseRedirect('/post/{pk}'.format(pk=post_obj.pk))

    context = {
        'form': form,
    }
    return render(request, 'comment_create.html', context)


def delete_comment(request, postpk, compk):
    check_user(request)
    comment_obj = get_object_or_404(Comment, pk=compk)

    if not request.user == comment_obj.post.user:
        raise Http404

    context = {
        'comment_obj': comment_obj,
        'postpk': postpk,
    }
    if request.method == 'POST':
        comment_obj.delete()
        return HttpResponseRedirect('/post/{pk}'.format(pk=postpk))

    return render(request, 'comment_delete_confirm.html', context)


def post_draft(request, pk=None):
    check_user(request)
    post = get_object_or_404(Post, pk=pk)
    post.post_status = 'post'
    post.create_date = timezone.now()
    post.save()
    return HttpResponseRedirect('/post/')
