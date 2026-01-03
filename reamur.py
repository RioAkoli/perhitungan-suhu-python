# Program Konversi Suhu - Reamur

print("\nProgram Konversi Temperatur (Reamur)\n")

Reamur = float(input("Masukkan suhu awal dalam Reamur: "))
print("Suhu Reamur adalah", Reamur, "Reamur")

# Reamur ke Celsius
Celsius = Reamur * 5/4
print("Suhu dari Reamur ke Celsius adalah", Celsius, "Celsius")

# Reamur ke Fahrenheit
Fahrenheit = (Celsius * 9/5) + 32
print("Suhu dari Reamur ke Fahrenheit adalah", Fahrenheit, "Fahrenheit")

# Reamur ke Kelvin
Kelvin = Celsius + 273.15
print("Suhu dari Reamur ke Kelvin adalah", Kelvin, "Kelvin")
