from django.http import JsonResponse
from django.shortcuts import render , redirect , get_object_or_404
from .models import Live_index , history , Articel , Contact , Comment
from django.contrib import messages
from .form import ContactForm , CommentForm
def index(request):
    about=Live_index.objects.all()
    historys=history.objects.all()
    articles = Articel.objects.all()
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('con_name')
        email = request.POST.get('con_email')
        message = request.POST.get('con_message')

        Contact.objects.create(name=name, email=email, message=message)
        return JsonResponse({'status': 'success'})

    else:
        form = ContactForm()
    return render(request, "index.html", {'about': about , 'historys':historys , 'articles': articles , 'form': form}  ) 



def articles(request):
    articles = Articel.objects.all()
    return render(request, 'articels.html', {'articles': articles})



def singleblog(request, slug):
    dit = get_object_or_404(Articel, slug=slug)
    articel_dit = Articel.objects.all()
    comments = dit.comments.filter(is_approved=True)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = dit
            new_comment.save()
            return redirect('singleblog', slug=slug)

    return render(request, "singleblog.html", {
        'dit': dit,
        'articel_dit': articel_dit,
        'comments': comments,
        'form': form
    })