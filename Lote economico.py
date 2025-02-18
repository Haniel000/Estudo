#Inserir valores
ca = 3000
cc = 130
cpa = 0.25
pu = 25

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


#Fileira C (e Contas)

c1 = a1/2*pu
c2 = a2/2*pu
c3 = a3/2*pu


#Fileira D (e Contas)

d1 = cpa*c1
d2 = cpa*c2
d3 = cpa*c3


#Fileira E

e1 = cc*b1
e2 = cc*b2
e3 = cc*b3


#Fileira F

f1 = d1+e1
f2 = d2+e2
f3 = d3+e3

print(f'Os resultados da fileira F são: {f1:.2f}, {f2:.2f}, {f3:.2f}')

print(f"{'Coluna A':<10} {'Coluna B':<15} {'Coluna C':<15} {'Coluna D':<15} {'Coluna E':<15} {'Coluna F':<15}")
print("-" * 85)
print(f"{a1:<10} {b1:<15.2f} {c1:<15.2f} {d1:<15.2f} {e1:<15.2f} {f1:<15.2f}")
print(f"{a2:<10.2f} {b2:<15.2f} {c2:<15.2f} {d2:<15.2f} {e2:<15.2f} {f2:<15.2f}")
print(f"{a1:<10} {b3:<15.2f} {c3:<15.2f} {d3:<15.2f} {e3:<15.2f} {f3:<15.2f}")
