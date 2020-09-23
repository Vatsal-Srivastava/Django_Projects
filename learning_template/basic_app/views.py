from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'text':'hello world','number':100,'fill':'This is random text to fill the space!'}
    return render(request, 'basic_app/index.html', context=my_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')