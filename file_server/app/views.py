import datetime
from pprint import pprint
from django.shortcuts import render
from os import listdir, stat
from os.path import abspath
import time

items = listdir('files')
m_time = [j.st_mtime for j in [stat('files/' + i) for i in items]]
c_time = [j.st_ctime for j in [stat('files/' + i) for i in items]]

result = (list(zip(items, m_time, c_time)))

files_list = []
for i in result:
    conf_dict = {}
    conf_dict['name'] = i[0]
    time_cortege_ctime = datetime.datetime(time.gmtime(int(i[1])).tm_year, time.gmtime(int(i[1])).tm_mon, time.gmtime(int(i[1])).tm_mday)
    time_cortege_mtime = datetime.datetime(time.gmtime(int(i[2])).tm_year, time.gmtime(int(i[2])).tm_mon, time.gmtime(int(i[2])).tm_mday)



    conf_dict['ctime'] = time_cortege_ctime
    conf_dict['mtime'] = time_cortege_mtime
    files_list.append(conf_dict)


def file_list(request, date=None):
    template_name = 'index.html'


    if date == None:
        context = {
            'files': files_list
            ,
            'date': date  # Этот параметр необязательный
        }
        return render(request, template_name, context)
    else:
        context = {
            'files': files_list
            ,
            'date': date
        }
        return render(request, template_name, context)


def file_content(request, name):
    text = []
    with open(f'files/{name}.txt', 'r', encoding='utf-8') as file:
        for string in file:
            text.append(string.strip('\n'))

        return render(
            request,
            'file_content.html',
            context={'file_name': name,
                     'file_content': text

            }
        )

