#Inserir valores
ca = float(input('Insira o CA (Custo Anual em Quantidades): '))
cc = float(input('Insira o CC (Custo de pedido de compra): '))
cpa = float(input('Insira o CPA (Custo de Material Armazenado): '))
pu = float(input('Insira o PU (Preço Unitário): '))

#Conta e Formula
lec = (2 * ca * cc) / (cpa * pu)
raiz_quadrada = lec ** 0.5

#Fileira do A
a1 = 100
a2 = raiz_quadrada
a3 = 1000

#Fileida B (e Contas)

b1 = ca/a1
b2 = ca/a2
b3 = ca/a3

print(f'Os resultados da fileira B são: {b1:.2f}, {b2:.2f}, {b3:.2f}')

#Fileira C (e Contas)

c1 = a1/2*pu
c2 = a2/2*pu
c3 = a3/2*pu

print(f'Os resultados da fileira C são: {c1:.2f}, {c2:.2f}, {c3:.2f}')

#Fileira D (e Contas)

d1 = cpa*c1
d2 = cpa*c2
d3 = cpa*c3

print(f'Os resultados da fileira D são: {d1:.2f}, {d2:.2f}, {d3:.2f}')