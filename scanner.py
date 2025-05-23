import socket

def scanear_portas(host, portasAlvo):
    print(f"\n[+] Iniciando scan em: {host}")
    for porta in portasAlvo:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            resultado = sock.connect_ex((host, porta))
            if resultado == 0:
                print(f"[ABERTA] Porta {porta} está aberta.")
            sock.close()
        except socket.gaierror:
            print(f"[ERRO] Host inválido: {host}")
            break
        except socket.error:
            print(f"[ERRO] Não foi possível conectar ao host: {host}")
            break

if __name__ == "__main__":
    print('Bem-vindo ao scanner de portas abertas.')
    targets = input("Digite os hosts (ex: 192.168.0.1, 192.168.0.2): ")
    lista_ips = [ip.strip() for ip in targets.split(",")]

    portasAlvo = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5432, 5900, 6379, 8080]

    for ip in lista_ips:
        scanear_portas(ip, portasAlvo)
