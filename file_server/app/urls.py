from django.urls import path, register_converter
from datetime import datetime
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.views import file_list, file_content


class ConverterFromStringInDatetime:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    format = '%Y-%m-%d'

    def to_python(self, date: str) -> datetime:

        date1 = datetime.strptime(date, self.format)

        return date1

    def to_url(self, value: datetime):
        value = str(int(value))
        return datetime.strftime(value, self.format)


register_converter(ConverterFromStringInDatetime, 'Dt')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<Dt:date>/', file_list, name='file_list'),

    path('file/<name>', file_content, name='file_content'),
]
