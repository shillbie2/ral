
from RAbotproses import LineBot

import threading


def login(resp, auth):

	bot = LineBot(resp, auth)


RL1 = threading.Thread(target=login, args=('Ei1','EqN5KfL3pcUkQJY9j3j4.GlJSvjS2pm9myo8QI5+91a.HMfFlAcy0rKJ8bLCMGMlwMVKpIjd/EMNQXb/qVgxCKI=')).start()

RL2 = threading.Thread(target=login, args=('Ei2','EqYAQT9hsD95Ko6ogTt8./L1lv4Aboo02War3v1Tu6a.e/0ovLXRIKfIxRaUyn/t/fEFvhYY/11UgVSwX3txS+M=')).start()

RL3 = threading.Thread(target=login, args=('Ei3','EqT59MZFfasvmIuf98e0.0QBPtPpsRPkXM8W0gdNeea.tvZqtE3sg/Wby/oo3KG7C71NB3VuK/jHVDGQ0Z2bXXs=')).start()

RL4 = threading.Thread(target=login, args=('Ei4','EqRefTpVpJa5X3o1gWO5.AVsLnXzsaFC9jZbNdLlEjq.PPLTA38xcHhseVlavhGj6T1aZ5H4wzPO1TxnMuvSZug=')).start()

RL5 = threading.Thread(target=login, args=('Ei5','Eqa4K51YfU1fgJbjA4q0.eEWgDZaU+phjaVYAhCanqa.lUUr0TsAksslj+mda1O3x/XowVyOztFBz4nR1TllF9U=')).start()

RL6 = threading.Thread(target=login, args=('Ei6','EqhR8Ff2Ngnm6d9UFp5d.ab7oSqvS7yXGluf91c3+lq.kwYje+mMmtW4WFqxx8x6cr+GpqnCswhvOxvAxJhvA9Y=')).start()

RL7 = threading.Thread(target=login, args=('Ei7','EqEeEQqewnVIiBgQdm3d.67ApbMEhUOpZAdUoTXOY7q.vvo+FNHkoKOEg9ME2SlWz9m5thFLbcIG1kxayzevdtg=')).start()

RL8 = threading.Thread(target=login, args=('Ei8','EqH1ghODXzk15ZAk3Fm9.U9B0NHrY4kn7ujdQduwdQq.IbBKlt/8Fe8I4m/n6oB30aQ58jMp1vtHx3LAlXB3cGo=')).start()

RL9 = threading.Thread(target=login, args=('Ei9','Eq3EI0QvKXqGAsUrbuo1.Np2pBFNiau38Fok/fG2BSq.C1htyHI6kUNyTWH3JLkrl3FYxCMDk2ol3eMIyYbbtso=')).start()

RL10 = threading.Thread(target=login, args=('Ei10','Eqdco4o4kOjkJmZyXNI8.e3aegds9M3gDTkNBRDMCAa.ibQ3L4HrolBoatl9Qv2V/gUaFok3gX/AlHzLxoiPw+M=')).start()



print('Login Berhasil!')
