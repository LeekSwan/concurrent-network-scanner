import argparse
import asyncio
import aioping
import ipaddress

############################
# Run this in cmd. Takes 3 arguments: subnet/mask, concurrency level, and timeout
# Only import from 3rd party is aioping: https://github.com/stellarbit/aioping
# Install using pip install aioping
# The rest of the imports are built-in

# Eg input: pingdiscover.py 192.168.0.0/24 --concurrent 5 --timeout 2

############################


async def ping_host(host_ip, timeout):
    try:
        delay = await aioping.ping(host_ip, timeout)
        print(host_ip, ": Ping response in %s ms" % delay, end=" | ")
    except TimeoutError:
        print(host_ip, ": Timed out", end=" | ")

parser = argparse.ArgumentParser(description='Ping based concurrent network scan.')
parser.add_argument('ip', metavar='S/M', type=str, nargs=1, help='E.g. "192.168.0.0/24"')
parser.add_argument('--concurrent', metavar='C', type=int, nargs="?", help='E.g. 8')
parser.add_argument('--timeout', metavar='T', type=int, nargs="?", const=5, help='E.g. 2')
args = parser.parse_args()

concur = args.concurrent
timeout = args.timeout
hosts = [str(ip) for ip in ipaddress.IPv4Network(args.ip[0])]
group_hosts = [hosts[i:i + concur] for i in range(0, len(hosts), concur)]

for groups in group_hosts:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([ping_host(ip, timeout) for ip in groups]))
    print("")


# test_group = ['google.com', 'amazon.com', 'cisco.com', 'facebook.com']
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([ping_host(ip, 2) for ip in test_group]))
