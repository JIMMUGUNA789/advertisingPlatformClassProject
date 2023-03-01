from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy


from .models import CompanyProfile, Reviews, Likes, Follows, CompanyImages
from posts.models import Post, PostComments
from django.core.paginator import Paginator
from django.contrib import messages

from django.db.models.functions import Random

from django.core.files.storage import default_storage
from django.views.generic.edit import UpdateView
from django.db.models import Avg
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from advertisements.models import Ad





# Create your views here.
def home(request):

    context = {}
    ads = Ad.objects.filter(adStatus='Active')
    if request.method == 'GET':
        searchTerm = request.GET.get('search')
        if searchTerm is not None:
            companies = CompanyProfile.objects.filter(
                Q(companyName__icontains=searchTerm) |
                Q(description__icontains=searchTerm) |
                Q(category__icontains=searchTerm) |
                Q(address__icontains=searchTerm)
                ).order_by('?')
            if len(companies) == 0:
                messages.error(request, "No companies found")
            for company in companies:
                avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                company.avg_rating = avg_rating
            context = {
                "companies":companies,
                "ads":ads

            }
        else:
            companies = CompanyProfile.objects.all().order_by('?')
            for company in companies:
                avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                company.avg_rating = avg_rating
                
            context = {
                "companies":companies,
                "ads":ads,
            }

    else:        
        companies = CompanyProfile.objects.all().order_by('?')
        for company in companies:
            avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
            company.avg_rating = avg_rating
            
        context = {
            "companies":companies,
            "ads":ads,
        }
    if request.method == 'POST':
        companylist = []
        category = request.POST['category']
        rating = request.POST.get('rating')
        if category is not None:
            if category == 'All':
                companies_subquery = CompanyProfile.objects.all().order_by('?')
                if rating is not None:
                     
                     for company in companies_subquery:
                        avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                        company.avg_rating = avg_rating  
                        if avg_rating is not None and avg_rating >= float(rating):
                            companylist.append(company)
                     companies = CompanyProfile.objects.filter(id__in=[item.id for item in companylist]).order_by('?')
                     for company in companies:
                        avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                        company.avg_rating = avg_rating            
                     context = {
                        "companies":companies,
                        "ads":ads,
                    }
                else:
                    companies = CompanyProfile.objects.all().order_by('?')
                    for company in companies:
                        avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                        company.avg_rating = avg_rating
                    context = {
                        "companies":companies,
                        "ads":ads,
                    }


              
            else:
                companies = CompanyProfile.objects.filter(category=category).order_by('?')
                if rating is not None:
                     companies_subquery = CompanyProfile.objects.filter(category=category).order_by('?')
                     for company in companies_subquery:
                        avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                        company.avg_rating = avg_rating  
                        if avg_rating is not None and avg_rating >= float(rating):
                            companylist.append(company)
                     companies = CompanyProfile.objects.filter(id__in=[item.id for item in companylist]).order_by('?')
                     for company in companies:
                        avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                        company.avg_rating = avg_rating            
                     context = {
                        "companies":companies,
                        "ads":ads,
                    }
                else:
                    companies = CompanyProfile.objects.all().order_by('?')
                    for company in companies:
                        avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                        company.avg_rating = avg_rating
                    context = {
                        "companies":companies,
                        "ads":ads,
                    }
                if len(companies) == 0:
                    messages.error(request, "No Business found in that category")
                for company in companies:
                    avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
                    company.avg_rating = avg_rating
                context = {
                    "companies":companies,
                    "ads":ads
                }
        
            
        
    return render(request, 'home.html', context)
    # company profile
def companyProfile(request, id):
    id = str(id)
    ads = Ad.objects.filter(adStatus='Active')

    company = CompanyProfile.objects.get(id=id)    
    posts = Post.objects.filter(company=id).order_by('-created_at')
    no_of_posts = Post.objects.filter(company=id).count()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # get the average rating of the company
    avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']

    
    
    context = {
        "company":company,
        "posts":page_obj,
        "no_of_posts":no_of_posts,
        "avg_rating":avg_rating,
        "ads":ads,
    }
    return render(request, 'company/companyProfile.html', context)

def companyPhotos(request, id):
    id = str(id)
    company = CompanyProfile.objects.get(id=id)
    posts = Post.objects.filter(company=id).order_by('?')
    images = CompanyImages.objects.filter(company=id).order_by('?')
    avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
    print(images)
    context = {
        "company":company,
        "posts":posts,
        "images":images,
        "avg_rating":avg_rating
    }
    return render(request, 'company/photos.html', context)

def reviews(request, id):
    id = str(id)
    ads = Ad.objects.filter(adStatus='Active')

    company = CompanyProfile.objects.get(id=id)
    posts = Post.objects.filter(company=id)
    reviews = Reviews.objects.filter(company=id).order_by('-created_at')
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
    context = {
        "reviews":page_obj,
        "company":company,
        "posts":posts,
        "avg_rating":avg_rating,
        "ads":ads,
    }
    return render(request, 'company/reviews.html', context)
@login_required(login_url='login')
def listCompany(request):
    if request.method == 'POST':
        companyName = request.POST['companyName']
        companyAdmin = request.user
        description = request.POST['description']
        profilePicture = request.FILES.get('profilePicture')      
        bannerPicture = request.FILES.get('bannerPicture')
        category = request.POST.get('category')
        phone = request.POST['phone']
        email = request.POST['email']
        websiteUrl = request.POST['websiteUrl']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        address = request.POST['address']        
        companyProfile = CompanyProfile(companyName=companyName, companyAdmin=companyAdmin, description=description, profilePicture=profilePicture, bannerPicture=bannerPicture, category=category, phone=phone, email=email, websiteUrl=websiteUrl, latitude=latitude, longitude=longitude, address=address)
        companyProfile.save()
        # register company as advitiser
        
      
        messages.success(request, 'Company profile created successfully')
        # redirect to the company profile page
        return redirect('companyProfile', id=companyProfile.id)
        
    
    return render(request, 'company/listCompany.html')

def addReview(request, id):
    id = str(id)
    company = CompanyProfile.objects.get(id=id)
    posts = Post.objects.filter(company=id)
    avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
    if request.method == 'POST':
        company = company
        user = request.user
        rating = request.POST['rating']
        review = request.POST['review']
        reviewPhoto = request.FILES.get('reviewPhoto')
        review = Reviews.objects.create(company=company, user=user, rating=rating, review=review, reviewPhoto=reviewPhoto)
        review.save()
        messages.success(request, 'Review added successfully')
        return redirect('reviews', id=id)
    context = {
        "company":company,
        "posts":posts,
        "avg_rating":avg_rating,
    }
    return render(request, 'company/addReview.html', context)

def likeAndDislikeCompany(request, company_id):
    company =  CompanyProfile.objects.get(id=company_id)
    user = request.user
    if Likes.objects.filter(company=company, user=user).exists():
        Likes.objects.filter(company=company, user=user).delete()
        messages.warning(request, 'You have disliked this company')
        return redirect('companyProfile', id=company_id)
    else:
        like = Likes.objects.create(company=company, user=user)
        like.save()
        messages.success(request, 'You have liked this company')
        return redirect('companyProfile', id=company_id)
def followAndUnfollowCompany(request, company_id):
    company =  CompanyProfile.objects.get(id=company_id)
    user = request.user
    if Follows.objects.filter(company=company, user=user).exists():
        Follows.objects.filter(company=company, user=user).delete()
        messages.warning(request, 'You have unfollowed this company')
        return redirect('companyProfile', id=company_id)
    else:
        follow = Follows.objects.create(company=company, user=user)
        follow.save()
        messages.success(request, 'You have followed this company')
        return redirect('companyProfile', id=company_id)

def addImages(request, id):
    id = str(id)
    company = CompanyProfile.objects.get(id=id)
    posts = Post.objects.filter(company=id)
    avg_rating = Reviews.objects.filter(company=company).aggregate(Avg('rating'))['rating__avg']
    if request.method == 'POST':
        company = company
        user = request.user        
        image = request.FILES.get('image')
        companyPhoto = CompanyImages(company=company, image=image)
        companyPhoto.save()
        messages.success(request, 'Image added successfully')
        return redirect('companyPhotos', id=id)
    context = {
        "company":company,
        "posts":posts,
        "avg_rating":avg_rating,
    }
    return render(request, 'company/addImages.html', context)

class CompanyProfileUpdate(UpdateView):
    model = CompanyProfile
    fields = [
        "companyName",
        "description",
        "profilePicture",
        "bannerPicture",
        "category",
        "phone",
        "email",
        "websiteUrl",
        "address"

    ]
    template_name = "company/updateCompanyProfile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = CompanyProfile.objects.get(id=self.object.id)
        avg_rating = Reviews.objects.filter(company=self.object).aggregate(Avg('rating'))['rating__avg']
        context['avg_rating'] = avg_rating
        return context

    def get_success_url(self):
        return reverse_lazy('companyProfile', kwargs={'id': self.object.id})
   
    
    
def digiverseSite(request):
    return render(request, 'index.html')