from models.cliente import Cliente
from models.conta import Conta


felicity: Cliente = Cliente('Felicity Jones', '123.456.789-01', '02/09/1981', 'felicity@gmail.com')
angelina: Cliente = Cliente('Angelina Jolie', '987.654.321-02', '21/12/1979', 'angelinajolie@gmail.com')

#  print(felicity)
# print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

# print(contaf)
# print(contaa)
