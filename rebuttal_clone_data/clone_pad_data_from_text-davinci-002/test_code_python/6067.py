def solution():
     total_pets = 36
     percent_dogs = 25
     percent_cats = 50
     percent_bunnies = 100 - (percent_dogs + percent_cats)
     num_bunnies = total_pets * (percent_bunnies / 100)
     result = num_bunnies
     
     return result

print(solution())