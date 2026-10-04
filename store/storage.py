from urllib.parse import quote

from django.conf import settings
from storages.backends.s3 import S3Storage


class SupabaseStorage(S3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        name = quote(name, safe='/')

        return (
            f"{settings.SUPABASE_PUBLIC_URL.rstrip('/')}"
            f"/storage/v1/object/public/"
            f"{settings.AWS_STORAGE_BUCKET_NAME}/"
            f"{name}"
        )