# Расчёт состава парэнтерального питания исходя из целевого объёма
# Количество энергии вычисляется по формуле: 150 ккал на 1 г аминоазота (1 г АА = 1 г белка / 6,25)
# Соотношение нутриентов вычисляется по формуле: 70% - глюкоза, 30% - жировые эмульсии

weight = int(input('Вес пациента: '))
volume = int(input('Целевой объём: '))
volume_tmp = 0
amin = 0

metab = int(input('Метаболическое соотношение: '))
concentr = int (input('Концентрация глюкозы: ')) / 100

while volume_tmp < volume-1: # Цикл подбора объёма
    amin = amin + 0.5 # Шаг цикла по подбору объёма
    kkal = ((amin) / 10 / 6.25) * metab  # Количество килокалорий
    glucose = ((kkal * 0.7) / 4) / concentr # Объём глюкозы нужной концентрации
    lipid = ((kkal * 0.3) / 9) / 0.2 # Объём жиров концентрации 20%
    volume_tmp = amin + glucose + lipid
else:
    print(f'Итоговый объём: ', volume_tmp)
    print(f'Глюкоза {concentr * 100}%: {round(glucose)} мл') # TODO перевод float в инт
    print(f'Липофундин 20%: {round(lipid)} мл')
    print(f'Аминовен 10%: {amin} мл')
    print(f'Белок: {round(amin / 10 / weight)} г/кг/сут, {round(kkal / weight)} ккал/кг/сут')
