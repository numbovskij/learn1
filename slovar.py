weather = {
	"city": "Москва",
	"temperature": "20",
	"wind": "восточный"
}

print(weather.get("city"))

weather["temperature"] = "30"

print(weather["temperature"])

n = 0

for element in weather:
	n = n + 1

print('Количество элементов в словаре weather = %s' % (n)) 

weather["date"] = "27.05.2021"

print(weather["date"])

"country" in weather 