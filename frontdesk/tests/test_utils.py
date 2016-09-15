import io

from django.test import TestCase

from frontdesk import utils


class ChecksumFileTests(TestCase):
    def setUp(self):
        self.octets = b'abcd'
        self.sample_file = io.BytesIO(self.octets)

    def test_default_sum_fmt_is_hex_md5(self):
        import hashlib
        algo = hashlib.md5()
        algo.update(self.octets)
        self.assertEquals(
            algo.hexdigest(),
            utils.checksum_file(self.sample_file)
        )

    def test_byte_offset_is_changed(self):
        former_offset = self.sample_file.tell()
        _ = utils.checksum_file(self.sample_file)
        self.assertNotEquals(former_offset, self.sample_file.tell())


class SafeChecksumFileTests(TestCase):
    def setUp(self):
        self.octets = b'abcd'
        self.sample_file = io.BytesIO(self.octets)

    def test_default_sum_fmt_is_hex_md5(self):
        import hashlib
        algo = hashlib.md5()
        algo.update(self.octets)
        self.assertEquals(
            algo.hexdigest(),
            utils.safe_checksum_file(self.sample_file)
        )

    def test_byte_offset_is_preserved(self):
        former_offset = self.sample_file.tell()
        _ = utils.safe_checksum_file(self.sample_file)
        self.assertEquals(former_offset, self.sample_file.tell())

