def get_Temperatur():
 while True:
C = input ("Gib die Temperatur in Celsius ein:")   
try:
C = float C
return C
except ValueError:
print("Nicht gültig")
def convert to kelvin():
K = C + 273,15
    return K
print("Das sind" +str(K) + "Kelvin")