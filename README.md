# Traceroute

Python implementation of traceroute command

## Help

```
Traceroute

positional arguments:
  destination           Destination host or IP address

options:
  -h, --help            show this help message and exit
  -m MAX_TTL, --max-ttl MAX_TTL
                        Maximum number of hops
  -w TIMEOUT, --timeout TIMEOUT
                        Timeout in seconds
```

## Examples

```
sudo venv/bin/python traceroute.py google.com
Tracing route to google.com over a maximum of 30 hops:
1	192.168.1.1
2	217.197.2.1
3	172.24.31.5
4	vunk-punk.rtr.pu.ru [172.24.25.32]
5	magma-vunk.rtr.pu.ru [172.24.25.38]
6	vlan3.kronos.pu.ru [195.70.196.3]
7	195.70.206.129
8	193-28-6-50.peering.pirix.ru [193.28.6.50]
9	74.125.244.180
10	72.14.232.85
11	142.251.61.221
12	216.239.58.69
13	Request timed out.
14	Request timed out.
15	Request timed out.
16	Request timed out.
17	Request timed out.
18	Request timed out.
19	Request timed out.
20	Request timed out.
21	Request timed out.
22	lu-in-f100.1e100.net [74.125.131.100]
```

```
sudo venv/bin/python traceroute.py google.com -m 2
Tracing route to google.com over a maximum of 2 hops:
1	192.168.1.1
2	217.197.2.1
Failed to reach google.com in 2 hops
```
