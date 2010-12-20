from django.db import transaction
from django.core.management import base
from django.contrib.admin import models as admin_models

from blog import models

def random(count):
    import random
    import string
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(count))

class Command(base.BaseCommand):

    @transaction.commit_on_success()
    def handle(self, *args, **options):
        users = admin_models.User.objects.all()
        for i in range(int(args[0])):
            user = users[0] if i % 2 == 0 else users[1]
            models.Blog.objects.create(user=user, title=random(50), content=random(200))
            models.Tweet.objects.create(user=user, title=random(50), tweet=random(140))