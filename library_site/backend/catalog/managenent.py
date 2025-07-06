from django.contrib.auth import get_user_model

def create_superuser():
    username, password = SUPERUSER_CREDENTIALS
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password)