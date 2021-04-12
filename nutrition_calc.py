veight = int(input('Целевой объём: '))
volume = int(input('Целевой объём: '))
volume_tmp = 0
amin = 0

metab = int(input('Метаболическое соотношение: '))
concentr = int (input('Концентрация глюкозы: ')) / 100

while volume_tmp < volume-1:
    amin = amin + 0.5
    kkal = ((amin) / 10 / 6.25) * metab
    glucose = ((kkal * 0.7) / 4) / concentr
    lipid = ((kkal * 0.3) / 9) / 0.2
    volume_tmp = amin + glucose + lipid
else:
    print(f'Итоговый объём: ', volume_tmp)
    print(f'Глюкоза {concentr * 100}%: {round(glucose)} мл')
    print(f'Липофундин 20%: {round(lipid)} мл')
    print(f'Аминовен 10%: {amin} мл')
