#Program Konversi Suhu

#Celcius 
print ("\nProgram Konversi Temperatur\n")

Celcius = float(input('Masukkan suhu awal dalam celcius: '))
print ("Suhu Celcius adalah", Celcius, "Celcius")

#Celcius ke reamur

Reamur = float (4/5 * Celcius)
print ("Suhu dari Celcius ke Reamur adalah", Reamur, "Reamur")

#Celcius ke Fahrenheit

Fahrenheit = float ((9/5 * Celcius) + 32)
print ("Suhu dari celcius ke Fahrenheit adalah", Fahrenheit, "Fahrenheit")

#Celcius ke Kelvin

Kelvin = float (Celcius + 273)
print ("Suhu dari celcius ke Kelvin adalah", Kelvin, "Kelvin")
