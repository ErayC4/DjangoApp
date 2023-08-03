from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostImage
from django.contrib.auth import login, logout, authenticate


def blog(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog.html', {'posts':posts})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post':post,
        'photos':photos
    })


def create_post(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        post = Post.objects.create(
            title=title,
            description=description
        )
        
        for file_num in range(0, int(length)):
            PostImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'create-post.html')


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    photos = PostImage.objects.filter(post=post)

    if request.method == 'POST':
        # Aktualisierte Daten aus dem Formular erhalten
        title = request.POST.get('title')
        description = request.POST.get('description')
        action = request.POST.get('action')

        if action == 'hide':
            post.hidden = True  # Setzen Sie das "hidden"-Feld auf "True"
        else:
            post.hidden = False  # Setzen Sie das "hidden"-Feld auf "False"

        post.title = title
        post.description = description
        post.save()

        # Handle image deletion
        delete_photo_ids = request.POST.getlist('delete_photo_ids')
        for photo_id in delete_photo_ids:
            photo = PostImage.objects.get(id=photo_id)
            photo.images.delete()  # Löschen Sie die Bilddatei aus dem Speicher
            photo.delete()  # Löschen Sie die PostImage-Instanz aus der Datenbank

        # Handle image uploads and updates
        for photo in photos:
            changed_photo = request.FILES.get(f'changed_photo_{photo.id}')
            if changed_photo:
                photo.images = changed_photo
                photo.save()

        return redirect('http://127.0.0.1:8000', id=post_id)

    return render(request, 'edit-post.html', {
        'post': post,
        'photos': photos
    })

"""
from .forms import RegistrationForm
def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('http://127.0.0.1:8000')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/sign-up.html', {"form":form})
"""