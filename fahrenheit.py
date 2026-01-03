#Program Konversi Suhu

#Fahrenheit 
print ("\nProgram Konversi Temperatur\n")

Fahrenheit = float(input('Masukkan suhu awal dalam Fahrenheit: '))
print ("Suhu Fahrenheit adalah", Fahrenheit, "Fahrenheit")

#Fahrenheit ke Celcius

Celcius = float ((Fahrenheit - 32) * 5/9)
print ("Suhu dari Celcius ke Celcius adalah", Celcius, "Celcius")

#Fahrenheit ke Kelvin

Kelvin = float (Celcius + 273)
print ("Suhu dari Fahrenheit ke kelvin adalah", Kelvin, "Kelvin")

#Fahrenheit ke Reamur

Reamur = float (4/9 * (Fahrenheit - 32))
print ("Suhu dari Fahrenheit ke Reamur adalah", Reamur, "Reamur")
