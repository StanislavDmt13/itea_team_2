from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from db.models import User, FriendRequest, Post
from django.db.models import Q


#                                                                               USER_PROFILE
def user_profile(request, user_id=None, *args, **kwargs):
    if request.user.is_authenticated:
        user = request.user
        friend_request_receiver = FriendRequest.objects.filter(sender=user)
        friend_request_sender = FriendRequest.objects.filter(receiver=user)
        friend_receiver = []
        friend_sender = []
        for item in friend_request_receiver:
            friend_receiver.append(item.receiver)
        for item in friend_request_sender:
            friend_sender.append(item.sender)
        if request.user.id == user_id or user_id is None:
            self_page = True
            context = {
                'self_page': self_page,
                'username': user.username,
                'email': user.email,
                'photo': user.photo,
                'phone': user.phone,
                'short_bio': user.short_bio,
                'get_friends_number': user.get_friends_number,
                'friend_receiver': friend_receiver,
                'friend_sender': friend_sender
            }
            return render(request, 'user_profile.html', context)

        if request.user.id != user_id:
            account = User.objects.get(pk=user_id)
            context = {
                'account': account,
                'username': account.username,
                'email': account.email,
                'photo': account.photo,
                'phone': account.phone,
                'friends': account.friends,
                'short_bio': account.short_bio,
                'hide_email': account.hide_email,
                'hide_phone': account.hide_phone,
                'get_friends_number': account.get_friends_number,
                'friend_receiver': friend_receiver,
                'friend_sender': friend_sender,
                'get_friends': account.get_friends
            }
            return render(request, 'user_profile.html', context)
    else:
        return HttpResponse('<h1> Please, Sign_in </h1>')


@login_required
def edit(request, *args, **kwargs):
    if request.method =='POST':
        u_form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')
    else:
        u_form = ProfileEditForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'edit.html', context)


#                                                                       FRIENDS_SYSTEM
def friends_list(request, user_id=None):
    if request.user.is_authenticated:
        user = request.user
        query = FriendRequest.objects.filter(receiver=user, status='send')
        counter = user.get_friends()
        query_result = list(map(lambda x: x.sender, query))
        friend_query_is_empty = False
        no_friends = True
        if len(counter) != 0:
            no_friends = False
        if len(query_result) == 0:
            friend_query_is_empty = True
        if request.user.id == user_id or user_id is None:
            self_page = True
            context = {
                'query_result': query_result,
                'self_page': self_page,
                'friend_query_is_empty': friend_query_is_empty,
                'no_friends': no_friends,
                'get_friends': user.get_friends,
                }
            return render(request, 'friends_list.html', context)

        if request.user.id != user_id:
            account = User.objects.get(pk=user_id)
            get_friends = account.get_friends()
            context = {
                'account': account,
                'get_friends': get_friends,
            }
            return render(request, 'friends_list.html', context,)


def send_invitation(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        sender = request.user
        receiver = User.objects.get(pk=user_id)
        friend_relations = FriendRequest.objects.create(sender=sender, receiver=receiver, status='send')
        return redirect(request.META.get('HTTP_REFERER'))


def accept_invitation(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        sender = User.objects.get(id=user_id)
        receiver = request.user
        friend_status = FriendRequest.objects.get(sender=sender, receiver=receiver)
        if friend_status.status == 'send':
            friend_status.status = 'accepted'
            friend_status.save()
    return redirect('friends_list')


def decline_invitation(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        sender = User.objects.get(id=user_id)
        receiver = request.user
        friend_status = FriendRequest.objects.get(sender=sender, receiver=receiver)
        friend_status.delete()

    return redirect('friends_list')


def remove_from_friends(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        sender = request.user
        receiver = User.objects.get(pk=user_id)
        friend_relations = FriendRequest.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        friend_relations.delete()
        return redirect(request.META.get("HTTP_REFERER"))


def search_user(request):
    if request.method == 'POST':
        query = request.POST['query']
        accounts = User.objects.filter(username__icontains=query) or User.objects.filter(email__icontains=query)
        context = {
            'query': query,
            'accounts': accounts
        }
        return render(request, 'search_user.html', context)
    else:
        return render(request, 'search_user.html')






