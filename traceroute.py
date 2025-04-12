from scapy.all import IP, ICMP, sr1
import socket
import time

def traceroute(destino, max_hops=30, timeout=2):
    try:
        destino_ip = socket.gethostbyname(destino)
        print(f"Destino: {destino} ({destino_ip})\nSaltos:")
    except socket.gaierror:
        print(" Error: No se pudo resolver el dominio.")
        return

    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=destino_ip, ttl=ttl) / ICMP()
        start = time.time()

        try:
            resp = sr1(pkt, verbose=0, timeout=timeout)
        except PermissionError:
            print(" Se requieren permisos de administrador para ejecutar este script (ICMP).")
            return

        end = time.time()

        if resp is None:
            print(f"{ttl}. * Tiempo agotado")
        else:
            ip = resp.src
            tiempo = round((end - start) * 1000, 2)
            try:
                host = socket.gethostbyaddr(ip)[0]
            except:
                host = "Desconocido"
            print(f"{ttl}. {ip} ({host}) - {tiempo} ms")
            if ip == destino_ip:
                break

if __name__ == "__main__":
    destino = input("Ingrese el dominio: ").strip()
    if destino:
        traceroute(destino)
    else:
        print("Debes ingresar un dominio válido.")
