
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm

# Create your views here.
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
	# items = Item.objects.filter(list=list_)
	error = None

	if request.method == 'POST':
		try:
			item = Item(text = request.POST['text'], list=list_) 
			item.full_clean()
			item.save()
			return redirect(list_)
			# return redirect('/lists/%d/' % (list_.id,))
			# Item.objects.create(text=request.POST['item_text'], list=list_)
		except ValidationError:
			error = "You can't have an empty list item!"
			
	return render(request,'list.html', {'list': list_, 'error': error})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		# list_.delete()
		error = "You can't have an empty list item!"
		return render(request, 'home.html', {"error": error})
	return redirect(list_)
	# return redirect('view_list', list_.id)
	# return redirect('/lists/%d/' % (list_.id,))

# def add_item(request, list_id):
# 	list_ = List.objects.get(id=list_id)
# 	Item.objects.create(text=request.POST['item_text'], list=list_)

# 	return redirect('/lists/%d/' % (list_.id,))
	

