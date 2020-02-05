from django import template

from yggl.models import YgCategory, YgTag, Bm, Yg

register = template.Library()


@register.simple_tag
def get_categories():
    return YgCategory.objects.all()


@register.simple_tag
def get_alltags():
    return YgTag.objects.all()


@register.simple_tag
def get_freqtags():
    return YgTag.objects.all()[0:12]


@register.simple_tag
def get_moretags():
    alltags = YgTag.objects.all()
    freqtags = alltags[0:12]
    moretags = [tag for tag in alltags if tag not in freqtags]
    return moretags


@register.simple_tag
def get_tags():
    alltags = YgTag.objects.all()
    freqtags = alltags[0:12]
    moretags = [tag for tag in alltags if tag not in freqtags]
    return {'freqtags':freqtags, 'moretags': moretags}


@register.simple_tag
def get_bm():
    return Bm.objects.all()




@register.simple_tag
def get_all_yg():
    return Yg.objects.all()


@register.simple_tag
def get_hotest_books(num=3):
    return Book.objects.order_by('-clicknum')[0:num]


@register.simple_tag
def get_related_books(pk, maxcount=6):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        book = Book.objects.first()
    return Book.objects.filter(category=book.category).exclude(pk=book.pk)[:maxcount]


@register.simple_tag
def get_tags_related_yg(ygpk, maxcount=6):
    try:
        yg = Yg.objects.get(pk=ygpk)
    except Yg.DoesNotExist:
        yg = Yg.objects.first()
    tags = yg.tags.all()
    related_books =set()
    for tag in tags:
        books = Yg.objects.filter(tags=tag)
        related_books.update(books)
    return list(related_books)[:maxcount]



@register.filter(name='range')
def my_range(number, p):
    return range(0, number)


@register.filter(name='get_styles')
def get_styles(value):
    styles = ['primary', 'success', 'warning', 'danger', 'info', 'dark', 'light', 'default']
    return styles[value % len(styles)]




