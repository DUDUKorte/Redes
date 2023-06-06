def gera_ip_da_subrede(end_ip, mask):
    ip = ''
    pref = end_ip
    ini = 1
    end = 254
    text_2 = ''
    for i in range(32-mask): 
        text_2 += '1'
    aux_text = ''
    text_2=  text_2.zfill(32)
    aux_num = 0

    for j in text_2:
        if aux_num == 8:
            aux_num = 0
            aux_text += '.'
            aux_text += j
            aux_num += 1
        else:
            aux_text += j
            aux_num += 1

    text_2 = aux_text

    lista = text_2.split('.')
    for y in lista:
        actual = int(y, 2) #exibe número de binário para inteiro
        for i in range(actual):
            print(i)

for ip in gera_ip_da_subrede('192.168.246.200',24):
    print(ip)