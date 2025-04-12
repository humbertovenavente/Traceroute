# Traceroute GUI (Python + Scapy + Tkinter)

Este proyecto es un script en Python que simula el comportamiento del comando `traceroute`, utilizando **Scapy** para enviar paquetes ICMP y **Tkinter** para proporcionar una interfaz gráfica (GUI).

---

## ¿Qué hace?

- Permite al usuario ingresar un dominio 
- Lista todos los **(hops)** por los que pasa un paquete hasta llegar al destino.
- Para cada salto muestra:
  - Dirección IP
  - Nombre del host (si se puede resolver)
  - Tiempo de respuesta en milisegundos
- Muestra `* Tiempo agotado` si un salto no responde.

---

## Tecnologías utilizadas

- Python 3.12
- [Scapy](https://scapy.net/) – para construir y enviar paquetes de red.
- Tkinter – para construir la interfaz gráfica.
- socket – para resolver direcciones y nombres.

---

## Requisitos

- Python 3.10 o superior
- Permisos de administrador para ejecutar ICMP (usar `sudo`)
- En Ubuntu:
  ```bash
  sudo apt install py
  
 hon3-tk libpcap-dev


## pasos para que funcione
python3 -m venv venv
source venv/bin/activate


pip install scapy
sudo apt install python3-tk libpcap-dev

sudo ./venv/bin/python traceroute.py
