from puresnmp import get

ip = '127.0.0.1'
community = 'public'
oid = '.1.3.6.1.2.1.1.1.0'  # only an example


result = get(ip, community, oid)

print(result.decode())
