from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
	search_query = request.GET.get('search', '')
	if search_query:
		classics = Classic.objects.filter(Q(title__icontains=search_query) | 
										  Q(series__icontains=search_query) |
										  Q(files__icontains=search_query) |
										  Q(gram__icontains=search_query) |
										  Q(price__icontains=search_query) |
										  Q(typebox__icontains=search_query) |
										  Q(lists__icontains=search_query))
		premiums = Premium.objects.filter(Q(title__icontains=search_query) | 
										  Q(series__icontains=search_query) |
										  Q(files__icontains=search_query) |
										  Q(gram__icontains=search_query) |
										  Q(price__icontains=search_query) |
										  Q(typebox__icontains=search_query) |
										  Q(lists__icontains=search_query))
	else:
		ids = 2
		title = Title.objects.all()
		titles = Title.objects.all()
		classics = Classic.objects.all()
		classic_img = ClassicImg.objects.all()
		classic_imgs = ClassicImg.objects.all()
		premiums = Premium.objects.all()
		premium_img = PremiumImg.objects.all()
		premium_imgs = PremiumImg.objects.all()
		manufacture = Manufactures.objects.all()
		manufactures = Manufactures.objects.all()
		block = Blocks.objects.all()
		blocks = Blocks.objects.all()
		type_box = TypeBox.objects.all()
		type_boxes = TypeBox.objects.all()
		slide_classic = Classic.objects.order_by('?')[:2]
		slide_premium = Premium.objects.order_by('?')[:3]
		top_numbers_left = TopNumbersLeft.objects.all()
		top_numbers_right = TopNumbersRight.objects.all()
		socials = Socials.objects.all()
		footer = Footer.objects.all()
	return render(request, 'vp/index.html', 
		context={
			'ids': ids,
			'title': title, 
			'titles': titles,
			'classics': classics, 
			'premiums': premiums, 
			'classic_img': classic_img, 
			'classic_imgs': classic_imgs, 
			'premium_img': premium_img, 
			'premium_imgs': premium_imgs,
			'manufacture': manufacture, 
			'manufactures': manufactures,
			'block': block,
			'blocks': blocks,
			'type_box': type_box,
			'type_boxes': type_boxes,
			'slide_classic': slide_classic,
			'slide_premium': slide_premium,
			'top_numbers_left': top_numbers_left, 
			'top_numbers_right': top_numbers_right,
			'socials': socials,
			'footer': footer
		})

def show_gifts(request):
	search_query = request.GET.get('search', '')
	if search_query:
		classics = Classic.objects.filter(Q(title__icontains=search_query) | 
										  Q(series__icontains=search_query) |
										  Q(files__icontains=search_query) |
										  Q(gram__icontains=search_query) |
										  Q(price__icontains=search_query) |
										  Q(typebox__icontains=search_query) |
										  Q(lists__icontains=search_query))
		premiums = Premium.objects.filter(Q(title__icontains=search_query) | 
										  Q(series__icontains=search_query) |
										  Q(files__icontains=search_query) |
										  Q(gram__icontains=search_query) |
										  Q(price__icontains=search_query) |
										  Q(typebox__icontains=search_query) |
										  Q(lists__icontains=search_query))
	else:
		ids = 4
		title = Title.objects.all()
		titles = Title.objects.all()
		classics = Classic.objects.all()
		classic_img = ClassicImg.objects.all()
		classic_imgs = ClassicImg.objects.all()
		premiums = Premium.objects.all()
		premium_img = PremiumImg.objects.all()
		premium_imgs = PremiumImg.objects.all()
		top_numbers_left = TopNumbersLeft.objects.all()
		top_numbers_right = TopNumbersRight.objects.all()
		socials = Socials.objects.all()
		footer = Footer.objects.all()
	return render(request, 'vp/gifts.html', 
		context={
			'ids': ids,
			'title': title, 
			'titles': titles,
			'classics': classics, 
			'premiums': premiums, 
			'classic_img': classic_img, 
			'classic_imgs': classic_imgs, 
			'premium_img': premium_img, 
			'premium_imgs': premium_imgs,
			'top_numbers_left': top_numbers_left, 
			'top_numbers_right': top_numbers_right,
			'socials': socials,
			'footer': footer
		})

def cl_more(request, slug):
	sweet = Sweets.objects.all()
	sweets = Sweets.objects.all()
	sweet_img = SweetsImg.objects.all()
	sweets_img = SweetsImg.objects.all()
	manufacture = Manufactures.objects.all()
	manufactures = Manufactures.objects.all()
	classic_img = ClassicImg.objects.all()
	classic_imgs = ClassicImg.objects.all()
	file = FilesLoad.objects.all()
	files = FilesLoad.objects.all()
	classic = Classic.objects.get(slug__iexact=slug)
	top_numbers_left = TopNumbersLeft.objects.all()
	top_numbers_right = TopNumbersRight.objects.all()
	socials = Socials.objects.all()
	footer = Footer.objects.all()
	return render(request, 'vp/classic.html', 
		context={
			'classic': classic, 
			'classic_img': classic_img, 
			'classic_imgs': classic_imgs, 
			'sweet': sweet, 
			'sweets': sweets, 
			'sweet_img': sweet_img, 
			'sweets_img': sweets_img, 
			'manufacture': manufacture, 
			'manufactures': manufactures, 
			'file': file, 
			'files': files,
			'top_numbers_left': top_numbers_left, 
			'top_numbers_right': top_numbers_right,
			'socials': socials,
			'footer': footer
		})

def pr_more(request, slug):
	sweet = Sweets.objects.all()
	sweets = Sweets.objects.all()
	sweet_img = SweetsImg.objects.all()
	sweets_img = SweetsImg.objects.all()
	manufacture = Manufactures.objects.all()
	manufactures = Manufactures.objects.all()
	premium_img = PremiumImg.objects.all()
	premium_imgs = PremiumImg.objects.all()
	file = FilesLoad.objects.all()
	files = FilesLoad.objects.all()
	premium = Premium.objects.get(slug__iexact=slug)
	top_numbers_left = TopNumbersLeft.objects.all()
	top_numbers_right = TopNumbersRight.objects.all()
	socials = Socials.objects.all()
	footer = Footer.objects.all()
	return render(request, 'vp/premium.html', 
		context={
			'premium': premium, 
			'premium_img': premium_img, 
			'premium_imgs': premium_imgs, 
			'sweet': sweet, 
			'sweets': sweets, 
			'sweet_img': sweet_img, 
			'sweets_img': sweets_img, 
			'manufacture': manufacture, 
			'manufactures': manufactures, 
			'file': file, 
			'files': files,
			'top_numbers_left': top_numbers_left, 
			'top_numbers_right': top_numbers_right,
			'socials': socials,
			'footer': footer
		})

def prices_input(request):
	ids = 5
	title = Title.objects.all()
	titles = Title.objects.all()
	classics = Classic.objects.all()
	classic_img = ClassicImg.objects.all()
	classic_imgs = ClassicImg.objects.all()
	premiums = Premium.objects.all()
	premium_img = PremiumImg.objects.all()
	premium_imgs = PremiumImg.objects.all()
	file = FilesLoad.objects.all()
	files = FilesLoad.objects.all()
	top_numbers_left = TopNumbersLeft.objects.all()
	top_numbers_right = TopNumbersRight.objects.all()
	socials = Socials.objects.all()
	footer = Footer.objects.all()
	return render(request, 'vp/prices.html',
		context={
			'ids': ids,
			'title': title, 
			'titles': titles,
			'classics': classics, 
			'premiums': premiums,
			'classic_img': classic_img, 
			'classic_imgs': classic_imgs, 
			'premium_img': premium_img, 
			'premium_imgs': premium_imgs,
			'file': file, 
			'files': files,
			'top_numbers_left': top_numbers_left, 
			'top_numbers_right': top_numbers_right,
			'socials': socials,
			'footer': footer
		})

def delivery_input(request):
	ids = 6
	title = Title.objects.all()
	titles = Title.objects.all()
	file = FilesLoad.objects.all()
	files = FilesLoad.objects.all()
	top_numbers_left = TopNumbersLeft.objects.all()
	top_numbers_right = TopNumbersRight.objects.all()
	socials = Socials.objects.all()
	footer = Footer.objects.all()
	return render(request, 'vp/buy.html',
		context={
			'ids': ids,
			'title': title, 
			'titles': titles,
			'file': file, 
			'files': files,
			'top_numbers_left': top_numbers_left, 
			'top_numbers_right': top_numbers_right,
			'socials': socials,
			'footer': footer
		})

def contacts_input(request):
	ids = 7
	title = Title.objects.all()
	titles = Title.objects.all()
	top_numbers_left = TopNumbersLeft.objects.all()
	top_numbers_right = TopNumbersRight.objects.all()
	socials = Socials.objects.all()
	footer = Footer.objects.all()
	return render(request, 'vp/contacts.html',
		context={
			'ids': ids,
			'title': title, 
			'titles': titles,
			'top_numbers_left': top_numbers_left, 
			'top_numbers_right': top_numbers_right,
			'socials': socials,
			'footer': footer
		})