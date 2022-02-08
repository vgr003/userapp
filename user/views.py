from django.shortcuts import render

from product.models import Product
from user.models import User, Post


def login(request):
    if request.method=='POST':
        error = ""
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username is ",username)
        print("password is ",password)
        if username == "admin" and password == "admin":
            user_list = User.objects.all()
            post_list = Post.objects.all()
            product_list = Product.objects.all()
            context = {
                'userlist':user_list,
                'postlist':post_list,
                'productlist':product_list,
            }
            return render(request,'dashboard.html',context)
        try:
            obj = User.objects.get(username=username, password=password)
            print('user:', obj)
            a_list = str(obj).split(" ")
            id = a_list[0]
            user = a_list[1]
            if str(user) == username:
                print("ok")
            return render(request, 'post.html', context={'id': id})
        except:
            error = "Invalid User!"
            context = {
                'error': error
            }
            return render(request, 'login.html', context)

    return render(request,'login.html')

def userPost(request):
    if request.method == 'POST':
        post = Post()
        post.user=User.objects.get(id=int(request.POST.get("id")))
        post.text=request.POST.get("text")
        post.created_at = request.POST.get("created_at")
        post.updated_at = request.POST.get("updated_at")
        post.save()
        return render(request,'post.html',context={'id':request.POST.get("id")})