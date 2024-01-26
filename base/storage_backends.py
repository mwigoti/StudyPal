# storage_backends.py

from django.core.files.storage import FileSystemStorage

class StaticStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        return name  # Prevent overwriting existing files
