def converttemperature(value, unit):
  if unit.upper() == 'C':
    return (value * 9/5 ) + 32
  elif unit.upper() == 'F':
    return (value - 32) * 9/5
  else:
    print ("Error")

angka = float(input("Masukan angka suhu = "))
unit = input("Masukan satuan (C atau F) = ")

hasil_akhir = converttemperature(angka, unit)
print ("Hasil Akhirnya adalah = ", hasil_akhir)