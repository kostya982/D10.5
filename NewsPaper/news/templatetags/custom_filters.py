from django import template

register = template.Library()

bad_words = ['редиска', 'хорошо', 'stupid']


@register.filter()
def censor(value):
    for bw in bad_words:
        try:
            value = value.lower().replace(bw.lower(), bw[0] + '*' * (len(bw) - 1))
        except AttributeError:
            print('Цензура не может быть применена к числам')
    return value


@register.filter()
def lenght(value):
    return len(value)
