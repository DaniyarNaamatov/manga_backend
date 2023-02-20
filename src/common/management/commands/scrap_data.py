from .utils import Scrap, create_genre
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Parsing manga"

    def handle(self, *args: any, **options: any) -> object:
        # create_genre(self)
        # Scrap.scrap_users()
        # Scrap.scrap_manga()
        Scrap.scrap_comments()
