def gera_ip_da_subrede(end_ip, mask):
    ips = end_ip.split('.')
    test = 0b11110000
    print(ips[0] & test)
    pref = end_ip
    ini = 1
    end = 254
    for i in range(ini,end+1):
        ip = f'{pref}.{i}'
        yield(ip)

for ip in gera_ip_da_subrede('192.168.246.200',28):
    print(ip)