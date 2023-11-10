import random
from django.core.management.base import BaseCommand

from faker import Faker

from blog.models import BlogPost

fake = Faker("uk")


class Command(BaseCommand):
    help = "Add demo blog posts"

    def handle(self, *args, **options):
        for _ in range(100):
            post_id = BlogPost.objects.create(
                title=fake.sentence(), content=fake.text(random.randint(1000, 3500))
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully added id: {post_id}"))
