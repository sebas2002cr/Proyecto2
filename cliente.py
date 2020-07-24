import socket
import threading
import json

puerto = 5050
servidor = socket.gethostbyname(socket.gethostname())
direccion = (servidor, puerto)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(direccion)


def mensaje_codificado(data, status):
    mensaje_json = {'data': data, 'status': status}
    mensaje_codificado = json.dumps(mensaje_json).encode('utf-8')
    return mensaje_codificado


def escuchar():
    while True:
        mensaje = cliente.recv(1024).decode('utf-8')
        if mensaje:
            mensaje_decodificado = json.loads(mensaje)
            print(mensaje_decodificado['data'])


def main():
    escucha = threading.Thread(target=escuchar)
    escucha.start()
    while True:
        data = input("(Tu): ")
        mensaje = mensaje_codificado(data, 'MSG')
        cliente.send(mensaje)


main()