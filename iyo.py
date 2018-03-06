from Sbproses import LineBot

import threading


def login(resp, auth):

	bot = LineBot(resp, auth)


Rio = threading.Thread(target=login, args=('.','Eqi6VbUB9QfQyGKNo8ob.w6+8YbOkbOMyiHAGbC+hcW.ji1ZNYCYvnppEWNECNSRaiKa47SJ4Bw+oQ2kVUrmyL0=')).start()

print('Login Berhasil!')