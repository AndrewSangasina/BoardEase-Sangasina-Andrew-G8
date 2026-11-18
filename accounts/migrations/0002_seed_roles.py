from django.db import migrations

def seed(apps, schema_editor):
    Role = apps.get_model("accounts", "Role")
    for n in ["Landlord", "Caretaker", "Tenant"]:
        Role.objects.get_or_create(role_name=n)

class Migration(migrations.Migration):
    dependencies = [("accounts", "0001_initial")]
    operations = [migrations.RunPython(seed)]