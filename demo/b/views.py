# coding: utf-8
from django.shortcuts import render,HttpResponse,render_to_response
from django import forms
from b.models import Img

# Create your views here.


# Create your views here.
class uploadImgForm(forms.Form):
    Img = forms.FileField()



def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def uploadImg(request):
    """
    upload image
    :param request:
    :return:
    """
    if request.method == 'POST':
        uf = uploadImgForm(request.POST,request.FILES)
        if uf.is_valid():
            img_path = uf.cleaned_data['Img']

            new_img = Img()
            new_img.img = img_path
            new_img.save()
            return HttpResponse('OK')
    else:
        uf=uploadImgForm()

    return render_to_response('uploadimg.html',{'uf':uf})

def showImg(request):
    """
    显示图片
    :param request:
    :return:
    """
    imgs = Img.objects.all()
    content = {'imgs':imgs}
    return render(request,'showimg.html',content)

