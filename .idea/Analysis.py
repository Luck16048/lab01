
#średnia
numbers = [10, 12, 14, 16]
total = sum(numbers)
average = sum(numbers) / len(numbers)


#medianę
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 1:
    mediane = sorted_numbers [n // 2]
else:
    mediane = (sorted_numbers [n // 2 -1] + sorted_numbers [n // 2]) / 2



#Min max
minimum = numbers[0]
maximum = numbers[0]
for n in numbers:
   if n < minimum:
       minimum = n
   elif n > maximum:
       maximum = n



#Ile ocen powyżej średniej
above_average = 0
for grade in numbers:
    if grade > average:
        above_average += 1



# Słownik z wynikami
results = {
    "Średnia": average,
    "Mediana": mediane,
    "Min": minimum,
    "Max": maximum,
    "Powyżej średniej": above_average
}

for klucz, wartość in results.items():
    print(f"{klucz}: {wartość}")