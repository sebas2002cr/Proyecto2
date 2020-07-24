import socket
import threading
import json
puerto = 5050

servidor = socket.gethostbyname(socket.gethostname())
status = {
    'desconectado':'DESC'
}

direccion = (servidor,puerto)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(direccion)

jugadores = []

def hiloJugador(con, dire):
    print(f"Jugador {dire} conectado")
    conectado = True
    while  conectado:
        mensaje = con.recv(1024).decode('utf-8')
        if mensaje:
            mensaje_decodificado = json.loads(mensaje)
            if mensaje_decodificado['status'] == status['desconectado']:
                conectado = False
                jugadores.remove(con)
                print(f'Jugador {dire} desconectado')
            broadcast(con,mensaje_decodificado)
            print(mensaje_decodificado)
    con.close()

def broadcast(desde,mensaje):
    for jugador in jugadores:
        if jugador!=desde:
            print(jugador, desde)
            jugador.send(json.dumps(mensaje).enconde('utf-8'))

def run():
    server.listen()
    while True:
        con, dire = server.accept()
        hilo = threading.Thread(target=hiloJugador,args=(con, dire))
        jugadores.append(con)
        hilo.start()
        print(f"[{len(jugadores)}]")

print("Server corriendo")
run()