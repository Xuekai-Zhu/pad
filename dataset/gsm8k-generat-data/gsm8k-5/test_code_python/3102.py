def solution():
    num_students = 20  # Mrs. Gable has 20 students in her class
    num_lunches = 20  # Mrs. Gable brought 20 lunches for the students
    num_animal_crackers_per_pack = 10  # Each pack of animal crackers contains 10 animal crackers

    # Calculate the total number of animal crackers in all the lunch bags
    total_animal_crackers = num_lunches * num_animal_crackers_per_pack

    # Calculate the number of animal crackers not eaten
    num_uneaten_animal_crackers = 2

    # Calculate the total number of animal crackers eaten
    num_eaten_animal_crackers = total_animal_crackers - (num_students * num_uneaten_animal_crackers)

    result = num_eaten_animal_crackers
    return result

print(solution())