
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm
from django.views.generic import FormView, CreateView

# Create your views here.
class HomePageView(FormView):
	"""docstring for HomePageView"""
	template_name = 'home.html'
	form_class = ItemForm
		
class NewListView(CreateView, HomePageView):

	def form_valid(self, form):
		# list_ = List.objects.create()
		# form.save(for_list=list_)
		# return redirect(list_)
		list = List.objects.create()
		Item.objects.create(text=form.cleaned_data['text'], list=list)
		return redirect('/lists/%d/' % (list.id,))


def home_page(request):
	# if request.method == 'POST':
	# 	return HttpResponse(request.POST['item_text'])
	# return render(request, 'home.html')
	# return HttpResponse('<html><title>To-Do lists</title></html>')

	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['item_text'])
	# 	return redirect('/lists/the-only-list-in-the-world/')
	return render(request,'home.html', {'form': ItemForm()})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	# form = ItemForm()
	form = ExistingListItemForm(for_list=list_)
	if request.method == 'POST':
		# form = ItemForm(data=request.POST)
		form = ExistingListItemForm(for_list=list_, data=request.POST)
		if form.is_valid():
			# Item.objects.create(text=request.POST['text'], list=list_)
			form.save()
			# form.save(for_list=list_)
			return redirect(list_)

	return render(request,'list.html', {'list': list_, 'form': form})


	# 	try:
	# 		item = Item(text = request.POST['text'], list=list_) 
	# 		item.full_clean()
	# 		item.save()
	# 		return redirect(list_)
	# 		# return redirect('/lists/%d/' % (list_.id,))
	# 		# Item.objects.create(text=request.POST['item_text'], list=list_)
	# 	except ValidationError:
	# 		error = "You can't have an empty list item, blin"
	
	# return render(request,'list.html', {'list': list_, 'error': error, 'form': form})

def new_list(request):
	form = ItemForm(data=request.POST) #;print(request.POST)
	if form.is_valid():
		list_ = List.objects.create()
		# Item.objects.create(text=request.POST['text'], list=list_)
		form.save(for_list=list_)
		return redirect(list_)
	else:
		return render(request, 'home.html', {"form": form})

	# list_ = List.objects.create()
	# item = Item.objects.create(text=request.POST['text'], list=list_)
	# try:
	# 	item.full_clean()
	# 	item.save()
	# except ValidationError:
	# 	list_.delete()
	# 	error = "You can't have an empty list item, blin"
	# 	return render(request, 'home.html', {"error": error})
	# return redirect(list_)

	# return redirect('view_list', list_.id)
	# return redirect('/lists/%d/' % (list_.id,))

# def add_item(request, list_id):
# 	list_ = List.objects.get(id=list_id)
# 	Item.objects.create(text=request.POST['item_text'], list=list_)

# 	return redirect('/lists/%d/' % (list_.id,))
	

