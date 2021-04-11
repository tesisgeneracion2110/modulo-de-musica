import music.song
import music.config
# import argparse
# import pythonosc
# from pythonosc import osc_server

song = music.song.Song(
    None,
    None,
    None,
    None,
    None,
    None,
    [
        ["intro", 1],
        ["chorus", 1]
    ]
)

"""
def osc_server():
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = pythonosc.dispatcher.Dispatcher()
  dispatcher.map("/port", print)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()


import threading

def contar():
    '''Contar hasta cien'''
    contador = 0
    while contador<100:
        contador+=1
        print('Hilo:',
              threading.current_thread().getName(),
              'con identificador:',
              threading.current_thread().ident,
              'Contador:', contador)

hilo1 = threading.Thread(target=music.config.prepare_song(song))
hilo2 = threading.Thread(target=contar)
hilo1.start()
hilo2.start()
"""

music.config.prepare_song(song)
# osc_server()
