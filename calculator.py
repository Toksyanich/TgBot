weight = int(input("Вес: "))
height = int(input("Рост: "))
age = int(input("Возраст: "))
print("Коэффициенты:")
print("\t1.2 - минимальный уровень физ нагрузки или полное ее отсутствие (сидячая работа, отсутствие спорта)")
print("\t1.3 - 1.4 - легкий уровень активности (легкие физические упражнения около 3 раз за неделю, ежедневная утренняя зарядка, пешие прогулки)")
print("\t1.5 - 1.6 - средняя активность (спорт до 5 раз за неделю)")
print("\t1.7 - 1.8 - Высокая активность (активный образ жизни с ежедневными интенсивными тренировками)")
print("\t1.9 - 2.0 - экстремально высокая активность(спортивный образ жизни, тяжелый физический труд, длительные тяжелые тренировки каждый день)")
koef = float(input("Коэффициент: "))

DCI = (weight + height - age) * koef

print((int (DCI)))