# Расчёт состава парэнтерального питания исходя из целевого объёма
# Количество энергии вычисляется по формуле: 150 ккал на 1 г аминоазота (1 г АА = 1 г белка / 6,25)
# Соотношение нутриентов вычисляется по формуле: 70% - глюкоза, 30% - жировые эмульсии

from math import ceil

weight = int(input('Вес пациента: '))
volume = int(input('Целевой объём: '))
volume_tmp = 0
amin = 0

metab = int(input('Метаболическое соотношение: '))
concentr = int(input('Концентрация глюкозы: '))

while volume_tmp < volume-1:  # Цикл подбора объёма
    amin = amin + 0.1  # Шаг цикла по подбору объёма
    kkal = (amin / 6.25 / 10) * metab  # Количество килокалорий
    glucose = ((kkal * 0.7) / 4) / (concentr / 100)  # Объём глюкозы нужной концентрации
    fat = ((kkal * 0.3) / 9) / 0.2  # Объём жиров концентрации 20%
    volume_tmp = amin + glucose + fat
else:
    print('================================')
    print(f'Итоговый объём: ', math.ceil(volume_tmp))
    print(f'Глюкоза {concentr}%: {round(glucose)} мл')
    print(f'Липофундин 20%: {round(fat)} мл')
    print(f'Аминовен 10%: {round(amin)} мл')
    print(f'Белок: {round((amin / 10 / weight),1)} г/кг/сут, {round(kkal / weight)} ккал/кг/сут')
