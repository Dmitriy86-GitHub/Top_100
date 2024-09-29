from django import template
import top_100_actresses.views as views
from top_100_actresses.models import Actresses

register = template.Library()


@register.filter(name='year')
def get_year(value):
    actresses = Actresses.objects.all()
    for actress in actresses:
        if value < 100:
            if value % 10 == 1:
                return 'год'
            elif value > 20 and (value % 10 == 3 or value % 10 == 4 or value % 10 == 2 or value % 10 == 2):
                return 'года'
            else:
                return 'лет'
        else:
            return 'Долгожитель'
