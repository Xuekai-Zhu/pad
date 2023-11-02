def solution():
    
    lunch_bags = 20
    animal_crackers_per_bag = 10
    total_animal_crackers = lunch_bags * animal_crackers_per_bag
    animal_crackers_not_eaten = 2 * animal_crackers_per_bag
    animal_crackers_eaten = total_animal_crackers - animal_crackers_not_eaten
    result = animal_crackers_eaten
    return result

print(solution())