import listings
from django.shortcuts import render
from listings.choices import state_choices,price_choices,bedroom_choices

from realtors.models import Realtor
from listings.models import Listing
# Create your views here.
def index(request):
  listings=Listing.objects.order_by('-list_date')[:3]
  
  context={
    'listings':listings,
    'state_choices':state_choices,
    'price_choices':price_choices,
    'bedroom_choices':bedroom_choices,

  }
  return render(request,'pages/index.html',context)

def about(request):
  realtors=Realtor.objects.all()

  mvp=Realtor.objects.filter(is_mvp=True)

  return render(request,'pages/about.html',{'realtors':realtors,'mvps':mvp,'length1':len(mvp)})
  
