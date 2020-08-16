import ipaddress
import unittest
from net_min import is_valid_ipv4, min_network


class TestMethods(unittest.TestCase):

    valid_ipv4_addresses = [
        '192.168.1.100',
        '10.0.0.1',
        '213.151.0.8',
        '77.77.77.77'
    ]

    invalid_ipv4_addresses = [
        '666.1.2.2',
        '256.256.256.256',
        '0.567.567.567',
        '192.168.0.257'
    ]

    def test_is_invalid_ip_addresses(self):

        for address in self.invalid_ipv4_addresses:
            status = is_valid_ipv4(address)
            self.assertFalse(status)

    def test_is_valid_ip_addresses(self):
        for address in self.valid_ipv4_addresses:
            status = is_valid_ipv4(address)
            self.assertTrue(status)

    def test_find_min_network(self):
        ip_list = ['192.168.0.0', '192.168.2.245', '192.168.255.255']
        self.assertEqual(min_network(ip_list),
                         ipaddress.IPv4Network('192.168.0.0/16'))


if __name__ == '__main__':
    unittest.main()
