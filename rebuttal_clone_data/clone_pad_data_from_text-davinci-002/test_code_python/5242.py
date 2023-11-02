def solution():
     initial_stuffed_animals = 10
     birthday_stuffed_animals = 2
     dad_stuffed_animals = (initial_stuffed_animals + birthday_stuffed_animals) * 3
     total_stuffed_animals = initial_stuffed_animals + birthday_stuffed_animals + dad_stuffed_animals
     result = total_stuffed_animals
     return result

print(solution())