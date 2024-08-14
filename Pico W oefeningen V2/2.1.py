# Probeer als oefening 1 "a and b are equal" te laten printen en oefening 2 "b is greater than a" te laten printen

a = 200
b = 33

# Dit is een if statement. Hier gaan wij 2 variable met elkaar verglijken d.m.v. een Comparison opperator. We gaan dus 2 variable met elkaar verglijken.
# Als de uitkomst van de verglijking "True" is dan gaan we de code eronder uitvoeren. Als deze "False" Dan slaan we de code over en gaan we door. 
if b > a:
  print("b is greater than a")
# Als de code boven niet is uitgevoerd boven dan word door de "elif" nog een check gedaan. Als deze "False" Dan slaan we de code over en gaan we door. 
elif a == b:
  print("a and b are equal")
# Als geen enkele statement hierboven "True"was dan word de "else"uitegoerd.   
else:
  print("a is greater than b")
  
  
# Lijst van Comparison opperator
# == 	Gelijk aan elkaar 				x == y 
# != 	Niet gelijk aan elkaar 			x != y 
# > 	Groter dan 						x > y 
# < 	Kleiner dan 					x < y 
# >= 	Groter dan of gelijk aan 		x >= y 
# <= 	Kleiner dan of gelijk aan 		x <= y

