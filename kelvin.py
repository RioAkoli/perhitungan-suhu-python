# Program Konversi Suhu - Kelvin

print("\nProgram Konversi Temperatur (Kelvin)\n")

Kelvin = float(input("Masukkan suhu awal dalam Kelvin: "))
print("Suhu Kelvin adalah", Kelvin, "Kelvin")

# Kelvin ke Celsius
Celsius = Kelvin - 273.15
print("Suhu dari Kelvin ke Celsius adalah", Celsius, "Celsius")

# Kelvin ke Fahrenheit
Fahrenheit = (Celsius * 9/5) + 32
print("Suhu dari Kelvin ke Fahrenheit adalah", Fahrenheit, "Fahrenheit")

# Kelvin ke Reamur
Reamur = Celsius * 4/5
print("Suhu dari Kelvin ke Reamur adalah", Reamur, "Reamur")
