def solution():
     ounces_per_dog = 6
     ounces_per_cat = 4
     ounces_per_rabbit = 1
     
     num_dogs = 6
     num_cats = 3
     num_rabbits = 1
     
     total_cleaner = (num_dogs * ounces_per_dog) + (num_cats * ounces_per_cat) + (num_rabbits * ounces_per_rabbit)
     result = total_cleaner
     
     return result

print(solution())