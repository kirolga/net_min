import sys
import ipaddress
import socket


def is_valid_ipv4(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def min_network(ip_addrs):
    for address in ip_addrs:
        if is_valid_ipv4(address) is False:
            raise ValueError('List contains invalid IP address')
    ip_addrs_iter = iter(ip_addrs)
    try:
        network_one = ipaddress.IPv4Network(ip_addrs_iter.__next__())
        network_two = ipaddress.IPv4Network(ip_addrs_iter.__next__())
    except StopIteration:
        raise ValueError('Please input at least 2 IP addresses')

    if network_one < network_two:
        min_net = network_one
        max_net = network_two
    else:
        min_net = network_two
        max_net = network_one

    for ip in ip_addrs_iter:
        network = ipaddress.IPv4Network(ip)
        if network < min_net:
            min_net = network
        if network > max_net:
            max_net = network
    ipnum = int(max_net[-1])
    prefixlen = max_net.prefixlen
    lowest_ipnum = int(min_net[0])
    width = 32

    while prefixlen > 0 and ipnum > lowest_ipnum:
        prefixlen -= 1
        ipnum &= -(1 << (width - prefixlen))

    return ipaddress.IPv4Network((ipnum, prefixlen))


if __name__ == '__main__':
    print('min net  ', min_network(sys.argv[1:]))
