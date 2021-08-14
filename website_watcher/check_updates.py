import re
import time
import requests
from datetime import date, datetime,timedelta

#clean all special characters from a string
def clean(value):
    value = re.sub('[^A-Za-z0-9\-_]+', '', value)
    return value


#clean all special characters from html code
def clean_html(value):
    value = re.sub('[^A-Za-z0-9\-_\`\~\!\@\#\$\%\^\&\*\(\)=\+\[\]\{\}|\\ ;\:\'\"\?\<\>\,\.\n/]+', '', value)
    return value


#given two strings, output any line in b that is not present in a
def difference(string_a,string_b):
    if string_a == string_b:
        return ""
    result = ""
    lines_a = string_a.split('\n')
    lines_b = string_b.split('\n')
    for line in lines_b:
        if not line in lines_a:
            result = result + line + '\n'
    return result


#retrieve an html document from the given url
def get_page(url):
    output = clean_html(requests.get(url).text).strip()
    return output

#given the url of a website, check if it has been updated, by comparing it to a reference snapshot
def check_updated(url):
    no_ref = 0
    try:
        ref_html = open('refs/%s.html' % clean(url),'r').read()
    except Exception as e:
        no_ref=1
        ref_html = ""
    new_html = get_page(url)
    if not no_ref:
       diff = difference(ref_html,new_html)
       #if len(diff) > 0:
       #    print(len(ref_html),len(new_html))
       return difference(ref_html,new_html)
    else:
       ref_file = open('refs/%s.html' % clean(url),'w')
       ref_file.write(new_html)
       ref_file.close()
       return ''  

#check all websites given in watchlist file
def check_all():
    watchlist = eval(open('watchlist').read())
    for key in watchlist.keys():
        updated = check_updated(watchlist[key])
        if len(updated) > 0:
           print("<h1> <a href='%s'> %s </a> </h1><br><br>" % (watchlist[key],key))
           print('<div>')
           print(updated)
           print('</div>')



