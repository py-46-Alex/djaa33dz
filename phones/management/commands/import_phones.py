import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

def npevrashator(word):
    word2 = ""
    for w in str(word):
        if w != ' ':
            word2 = word2 + w
        elif w == " ":
            word2 = word2 + '-'
    return word2
#
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            Phone.objects.create(id=phone.get('id'),
                                 name=phone.get('name'),
                                 price=phone.get('price'),
                                 image=phone.get('image'),
                                 release_date=phone.get('release_date'),
                                 lte_exists=phone.get('lte_exists'),
                                 slug=npevrashator(phone.get('name')))
            # print(phone)
            # TODO: Добавьте сохранение модели
            # pass
#
