def get_vat(payment):
	try:
		payment = float(payment)
		vat = payment / 100 * 18
		return round(vat, 2)
	except (TypeError, ValueError):
		print("Нет")

result = get_vat("adfad")

print ('Сумма НДС: %s' % (result))