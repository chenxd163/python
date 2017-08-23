from django.shortcuts import render
from booktest.models import BookInfo
# Create your views here.


def index(request):
    '''
    显示图书信息页面
    '''
    # 1.查找数据表中的图书信息
    book_list = BookInfo.objects.all()
    # 2.传递数据给模板文件
    return render(request, 'index.html', {'book_list': book_list})


def detail(resqust, bid):
    # 先找到这本书
    book = BookInfo.objects.get(id=int(bid))
    # 通过书去找英雄
    hero_list = book.heroinfo_set.all()

    return render(resqust, 'detail.html', {'book': book, 'hero_list': hero_list})



