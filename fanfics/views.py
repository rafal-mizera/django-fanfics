from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import PublicationForm, CommentForm
from .models import Publication, Comment
from taggit.models import Tag
from collections import defaultdict

# Create your views here.
def home(request):
    publications = Publication.objects.all()
    tags = defaultdict(int)
    for publication in publications:
        for name in publication.tags.names():
            tags[name] += 1
    tags = dict(tags)

    return render(request,'fanfics/home.html',{'tags': tags})


@login_required
def new_publication(request):
    if request.method == "POST":
        publication_form = PublicationForm(request.POST)
        if publication_form.is_valid():
            new_item = publication_form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            publication_form.save_m2m()
            return redirect("/fanfics/home")
    else:
        publication_form = PublicationForm()

    return render(request,'fanfics/new_publication.html',{'publication_form': publication_form})

def publications(request,tag_slug=None):
    publications = Publication.objects.all().order_by('-created')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        publications = publications.filter(tags__in=[tag])
    paginator = Paginator(publications,5)
    page = request.GET.get('page')
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)
    return render(request,'fanfics/publications.html',{'page': page,'publications': publications,'tag': tag})


def publication_details(request, year, month, day, publication):
    publication = get_object_or_404(Publication, slug=publication,created__year=year,created__month=month,created__day=day)
    comments = publication.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.publication = publication
            new_comment.save()
    else:
        comment_form = CommentForm()

    post_tags_ids = publication.tags.values_list('id',flat=True)
    similar_publications = Publication.objects.all().filter(tags__in=post_tags_ids).exclude(id=publication.id)
    similar_publications = similar_publications.annotate(same_tags=Count('tags')).order_by('-same_tags','-created')[:4]

    return render(request,'fanfics/details.html', {'publication': publication, 'comments': comments, 'comment_form': comment_form, 'similar_publications': similar_publications})

def publications_by_user(request,name):
    publications = Publication.objects.all()
    user = User.objects.get(username=name)
    user_publications = publications.filter(user=user)
    return render(request,
                  'fanfics/publications_by_user.html',
                  {'user_publications': user_publications, 'user': user})


@login_required
@require_POST
def publication_like(request):
    publication_id = request.POST.get('id')
    action = request.POST.get('action')
    if publication_id and action:
        try:
            publication = Publication.objects.get(id=publication_id)
            if action == 'like':
                publication.users_like.add(request.user)
            else:
                publication.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ok'})

def best_publications(request):
    best = Publication.objects.annotate(user_likes=Count('users_like')).order_by('-user_likes')[:10]
    return render(request,'fanfics/best_publications.html',{'best': best})
