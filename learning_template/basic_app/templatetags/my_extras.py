from django import template
register = template.Library()

# @register.filter(name='cut')
def vatsal(value,arg):
    '''
    this cuts out all the values of "args" from the string!
    '''
    return value.replace(arg,'*')

register.filter('vatsal',vatsal)