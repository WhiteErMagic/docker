from books.models import Book
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_page(request, pubdate):
    template = 'books/books_page.html'
    dates = Book.objects.values('pub_date')
    pages = []
    for d in dates:
        d_str = "{:%Y-%m-%d}".format(d['pub_date'])
        if not d_str in pages:
            pages.append(d_str)
    pages.sort()
    books = Book.objects.all().filter(pub_date=pubdate)
    paginator = Paginator(pages, 1)
    number_page = request.GET.get('page', pages.index(pubdate)+1)

    page = paginator.get_page(number_page)
    if len(page.paginator.object_list) > number_page:
        page_next = page.paginator.object_list[number_page]
    else:
        page_next = ''

    if 1 == number_page:
        page_prev = ''
    else:
        page_prev = page.paginator.object_list[number_page - 2]

    context = {
        'page_prev': page_prev,
        'page_next': page_next,
        'page_cur': page.paginator.object_list[number_page-1],
        'page': page,
        'books': books
    }
    return render(request, template, context)
