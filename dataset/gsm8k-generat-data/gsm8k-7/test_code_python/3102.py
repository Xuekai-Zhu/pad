def solution():
    num_students = 20
    num_lunches = 20
    animal_crackers_per_lunch = 10

    # Calculate the total number of animal crackers in all lunch bags
    total_animal_crackers = num_lunches * animal_crackers_per_lunch

    # Calculate the number of animal crackers that were not eaten
    num_uneaten_animal_crackers = 2 * animal_crackers_per_lunch

    # Calculate the number of animal crackers that were eaten
    num_eaten_animal_crackers = total_animal_crackers - num_uneaten_animal_crackers
    result = num_eaten_animal_crackers
    return result

print(solution())