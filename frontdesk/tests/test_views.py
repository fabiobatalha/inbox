import os

from django.test import TestCase, RequestFactory
from django.urls import reverse

from frontdesk import views, utils


class DepositPackageTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('frontdesk:deposits')

    def test_bright_path(self):
        """Testa o caminho feliz.
        """
        with open(os.path.abspath(__file__), 'rb') as _file:
            md5_sum = utils.safe_checksum_file(_file)
            request = self.factory.post(
                self.url,
                {'md5_sum': md5_sum, 'package': _file, 'depositor': 'gn1'}
            )

        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 200)

    def test_missing_md5_sum(self):
        with open(os.path.abspath(__file__), 'rb') as _file:
            request = self.factory.post(
                    self.url, {'package': _file})

        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 400)

    def test_missing_package(self):
        with open(os.path.abspath(__file__), 'rb') as _file:
            md5_sum = utils.safe_checksum_file(_file)
            request = self.factory.post(
                    self.url, {'md5_sum': md5_sum})

        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 400)

    def test_missing_all_data(self):
        with open(os.path.abspath(__file__), 'rb') as _file:
            request = self.factory.post(
                    self.url, {})

        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 400)

    def test_mismatching_package_checksum(self):
        with open(os.path.abspath(__file__), 'rb') as _file:
            md5_sum = utils.safe_checksum_file(_file)[::-1]  # só para zoar a soma
            request = self.factory.post(
                    self.url, {'md5_sum': md5_sum, 'package': _file})

        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 400)

    def test_get_request(self):
        request = self.factory.get(self.url)
        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 405)  # método http não permitido

    def test_put_request(self):
        request = self.factory.put(self.url, {})
        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 405)  # método http não permitido

    def test_delete_request(self):
        request = self.factory.delete(self.url)
        response = views.deposit_package(request)
        self.assertEqual(response.status_code, 405)  # método http não permitido

