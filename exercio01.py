print('='*30)
print('{:^30}'.format('TECH VISTORIAS - CONTROLE'))
print('='*30)

reprovado = 0
aprovado = 0
soma_anos = 0

total_veiculos = int(input('Quantos veiculos serão analisados? '))
for c in range(1, total_veiculos + 1):
    print(f'\n--- {c}° VEÍCULO ---')
    modelo = str(input('Modelo: ')).strip()
    ano = int(input('Ano de fabricação: '))
    pneus = int(input('Status dos pneus [1-Bom | 2-Irregular | 3-Ruim]: '))

    if ano < 2010:
        print('Atenção: Veículo antigo, verificar chassi com rigor')
    if pneus == 3:
        reprovado += 1
        print('Veículo reprovado. \nCausa: Pneu irregular.')
    else:
        aprovado += 1
        print('Veículo aprovado. Parabéns')
    soma_anos += ano
if total_veiculos > 0:
    media_idade = soma_anos / total_veiculos
    porcentagem = (reprovado / total_veiculos) * 100
else:
    media_idade = 0
    porcentagem = 0

# TOTAL DE VEÍCULOS
print('_'*30)
print('\n' + ' INTERRUPÇÃO DE FLUXO '.center(30, '='))
print(f'Foram feitas {total_veiculos} vistoria(s) hoje!')
print(f'Foram aprovados {aprovado}, e reprovados {reprovado}')
print(f'A média de idade da frota é {media_idade:.0f}')
print(f'A porcentagem de reprovados foram {porcentagem:.0f}%')
print('_'*30)