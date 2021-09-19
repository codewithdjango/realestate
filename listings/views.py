from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .choices import state_choices,price_choices,bedroom_choices

# Create your views here.

def index(request):
  listings=Listing.objects.all()
  paginator=Paginator(listings,3)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  return render(request,'listings/listings.html',{'listings':paged_listings,'state_choices':state_choices})

def listing(request, listing_id):
  listing=get_object_or_404(Listing,pk=listing_id)
  return render(request,'listings/listing.html',{'listing':listing})

def search(request):

  queryset_list=Listing.objects.order_by('-list_date')

  #keywords
  if 'keywords' in request.GET:
    keywords=request.GET['keywords']
    if keywords:
      queryset_list=queryset_list.filter(description__icontains=keywords)

  if 'city' in request.GET:
    city=request.GET['city']
    if city:
      queryset_list=queryset_list.filter(city__iexact=city)
  
  if 'state' in request.GET:
    state=request.GET['state']

    if state:
      queryset_list=queryset_list.filter(state__iexact=state)
      state_key=state

  if 'bedrooms' in request.GET:
    bedrooms=request.GET['bedrooms']
    if bedrooms:
      queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)

  if 'price' in request.GET:
    price=request.GET['price']
    if price:
      queryset_list=queryset_list.filter(price__lte=price)

      
  context={
    
    'state_choices':state_choices,
    'price_choices':price_choices,
    'bedroom_choices':bedroom_choices,
    'listings':queryset_list,
    'values': request.GET
  }

  
  return render(request,'listings/search.html',context)