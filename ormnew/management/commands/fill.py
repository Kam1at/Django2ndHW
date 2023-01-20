from django.core.management import BaseCommand
from ormnew.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category = [
            {'name': 'Фрукты', 'description': 'Вкусные фрукты'},
            {'name': 'Овощи', 'description': 'Сочные овощи'},
            {'name': 'Молочная продукция', 'description': 'Жирненькое молочко'},
            {'name': 'Хлебобулочные изделия', 'description': 'Наисвежайший хлеб и булочки'}
        ]

        category_list = []
        for item in category:
            category_list.append(
                Category(**item)
            )
        Category.objects.bulk_create(category_list)
