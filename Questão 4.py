m2 = float(input('Qla a área (m²) a ser pintada? '))
preco = 80
cobertura = 3 * 18
qnt = None
if m2 % cobertura == 0:
    qnt = m2 // cobertura
else:
    qnt = (m2 // cobertura) + 1

print(f'''Você precisará de {qnt} latas de tinta para cobrir uma área de {m2}m².
O custo total da compra será de R$ {(preco * qnt):.2f}''')
