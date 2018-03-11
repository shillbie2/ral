
from RAbotproses import LineBot

import threading


def login(resp, auth):

	bot = LineBot(resp, auth)


RL1 = threading.Thread(target=login, args=('Pay','EqMzAjoBiwuHTRcHszK2.T/UQKwNuh4JaPGysNhcrWG.f9gn0iqpJNgevwJ/FOmRF/66zVikZOodleFMfoHr7ZY=')).start()

RL2 = threading.Thread(target=login, args=('Pay2','EqqTUoYfk8aRThPBx8Bb.pcuGlGcp/NnqVWAB3oACcW.Iw/HnoAB5X38eusjT8BpAGk2YhTbs6vNk0f09vEIn1k=')).start()

RL3 = threading.Thread(target=login, args=('Pay3','EqREOUAKC9dOQ8W2Uuc1.qt+bJ4+ekdSryq5qpUxreq.UszPnLcX4/Wp3Xb9q02IpaYaElqK0/kV+fD4FqFclJI=')).start()

RL4 = threading.Thread(target=login, args=('Pay4','Eq4v8TfDfeBgcAVeeBD2.QBxU/UiA+rum5VK72Q6MuG.M85I+DZlfN3lzskdK+LHG38ri4EHD3Rd6cL+9zus3qc=')).start()

RL5 = threading.Thread(target=login, args=('Pay5','Eq1gXk4sNM8cZkO3AMC7.RU5viiSqnS9uDrZFSfwzLW.caaKTjm2kLEJ0kQwoQTE2jCJYkVHWMFCMmJxDYJzxT4=')).start()

RL6 = threading.Thread(target=login, args=('Pay6','EqvSjFFXzUFYm1VKpzP4.2A/w10/Gv/ToyJPYMsz7va.Hf1zDfsGay6FZLmIZWMwqj1JtsbQLhYyMZOrC1Shq9I=')).start()

RL7 = threading.Thread(target=login, args=('Pay7','EqCWmlA9QIF4dFgzqLH9.wyr0gyQ/wZaV9bNyxXClAq.XUeHeIjf4DoTPLGh2LhR7eDbHtm+tCHRaa/3tOlT6Is=')).start()

RL8 = threading.Thread(target=login, args=('Pay8','EqlaR1fvu40bqtBeg8Z4.+6PaZdrn0+rTdZ0wtrZZHa.1Rjt1GoTPfE7OPxAuTLgnA0ywBRjKiO22YszrndWrA8=')).start()

RL9 = threading.Thread(target=login, args=('Pay9','Eq4RgdEQeKrf6X52lJxc.v9ChN02kPEkSRXsJVpRJFa.HXapX1KFbeQPw6w6gJ7t/nsW+YV7uKE04wEPWGvaflg=')).start()

RL10 = threading.Thread(target=login, args=('Pay10','EqDGxOUpGgl8iy5E9rC2.lLY0pEIIyy0Ep1lHwFVz0G.TXeLTlCwvqNJebI9JLMPudCk5P8dS1sqAl/Up9TYyVQ=')).start()

RL11 = threading.Thread(target=login, args=('Pay11','EqDaoznpRSD5zCugvZZ7.Dx5ayqwgjzZp83UUVYqO9W.WmnYomO9b9DmALcqWKxIp7CPzcZ8FRsYeSShw+3EOZk=')).start()


print('Login Berhasil!')
