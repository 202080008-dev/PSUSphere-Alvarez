from django.test import TestCase
from django.conf import settings
from django.contrib.sites.models import Site


class SiteConfigTest(TestCase):
    def test_default_site_created(self):
        site = Site.objects.get(id=settings.SITE_ID)
        self.assertIsNotNone(site)
        self.assertTrue(site.domain)
        self.assertTrue(site.name)

    def test_accounts_login_resolves(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

