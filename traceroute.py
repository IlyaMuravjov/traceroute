import argparse
import socket

import scapy.layers.inet
import scapy.sendrecv


def check_positive_int(value: str) -> int:
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError(f'{n} is not a positive integer')
    return n


def check_adr(value: str) -> str:
    try:
        socket.gethostbyname(value)
        return value
    except socket.gaierror:
        raise argparse.ArgumentTypeError(f'unable to resolve host {value}')


def parse_traceroute_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Traceroute')
    parser.add_argument('destination', type=check_adr, help='Destination host or IP address')
    parser.add_argument('-m', '--max-ttl', type=check_positive_int, default=30, help='Maximum number of hops')
    parser.add_argument('-w', '--timeout', type=check_positive_int, default=5, help='Timeout in seconds')
    return parser.parse_args()


def concat_hostname_in_front_of_address(ip_address: str) -> str:
    try:
        (name, _, _) = socket.gethostbyaddr(ip_address)
        return f'{name} [{ip_address}]'
    except socket.herror:
        return ip_address


def traceroute():
    args = parse_traceroute_arguments()
    dst_ip = socket.gethostbyname(args.destination)
    print(f'Tracing route to {args.destination} '
          f'over a maximum of {args.max_ttl} hops:')
    for cur_ttl in range(1, args.max_ttl + 1):
        response = scapy.sendrecv.sr1(
            scapy.layers.inet.IP(dst=dst_ip, ttl=cur_ttl) / scapy.layers.inet.ICMP(),
            timeout=args.timeout,
            verbose=0
        )
        print(f'{cur_ttl}\t' +
              ('Request timed out.' if response is None
               else concat_hostname_in_front_of_address(response.src)))
        if response is not None and response.type == 0:
            return
    print(f'Failed to reach {args.destination} in {args.max_ttl} hops')


if __name__ == '__main__':
    traceroute()
