from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

# fila_teste = FilaNormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(1))
print(fila_teste_2.chama_cliente(5))
print(fila_teste_2.estatistica('10/10/2023', 182, 'detail'))
