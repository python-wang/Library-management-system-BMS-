from django.shortcuts import render,redirect,HttpResponse
from book import models

# Create your views here.

def index(request):  #首页
    ret = models.Book.objects.all().exists()  # 判断表是否有记录
    if ret:
        book_list=models.Book.objects.all()  # 查询表的所有记录
        return render(request,"index.html",{"book_list":book_list})
    else:
        hint = '<script>alert("没有书籍，请添加书籍");window.location.href="/books/add"</script>'
        return HttpResponse(hint)  # js跳转到添加页面

def add(request):  # 添加
    if request.method=="POST":
        # print(request.POST)
        title=request.POST.get("title")
        price=request.POST.get("price")
        pub_date=request.POST.get("pub_date")
        publish=request.POST.get("publish")
        is_pub=request.POST.get("is_pub")
        #插入一条记录
        obj=models.Book.objects.create(title=title,price=price,publish=publish,pub_date=pub_date,is_pub=is_pub)
        print(obj.title)

        hint = '<script>alert("添加成功");window.location.href="/index/"</script>'
        return HttpResponse(hint)  # js跳转到首页

    return render(request,"add.html")  # 默认渲染添加页面

def delete(request,id):  # 删除
    ret = models.Book.objects.filter(id=id).delete()  # 返回元组
    if ret[0]:  # 取值为1的情况下
        hint = '<script>alert("删除成功");window.location.href="/index/"</script>'
        return HttpResponse(hint)
    else:  # 取值为0的情况下
        hint = '<script>alert("删除失败");window.location.href="/index/"</script>'
        return HttpResponse(hint)

def manage(request):  # 管理页面
    ret = models.Book.objects.all().exists()
    if ret:
        book_list = models.Book.objects.all()
        #加载管理页面
        return render(request, "manage.html", {"book_list": book_list})
    else:
        hint = '<script>alert("没有书籍，请添加书籍");window.location.href="/books/add"</script>'
        return HttpResponse(hint)

def modify(request,id):  # 修改
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        is_pub = request.POST.get("is_pub")
        #更新一条记录
        ret = models.Book.objects.filter(id=id).update(title=title, price=price, publish=publish, pub_date=pub_date, is_pub=is_pub)
        # print(ret)

        if ret:  # 判断返回值为1
            hint = '<script>alert("修改成功");window.location.href="/index/"</script>'
            return HttpResponse(hint)  # js跳转
        else:  # 返回为0
            hint = '<script>alert("修改失败");window.location.href="/index/"</script>'
            return HttpResponse(hint)  # js跳转

    book = models.Book.objects.get(id=id)  # 默认获取id值
    return render(request, "modify.html", {"book": book})  # 渲染指定id的记录