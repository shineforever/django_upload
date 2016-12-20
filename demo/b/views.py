# coding: utf-8
from django.shortcuts import render
from b.models import Img

# Create your views here.
def uploadImg(request):
    """
    upload image
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_img = request.FILES.get('img')
        new_img.save()
    return render(request,'b/uploadimg.html')

def showImg(request):
    """
    显示图片
    :param request:
    :return:
    """
    imgs = Img.objects.all()
    content = {'imgs':imgs}
    return render(request,'b/showimg.html',content)

