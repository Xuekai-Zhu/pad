def solution():
    # Calculate the total number of animal crackers
    total_animal_crackers = 20 * 10  # 20 lunches with 10 animal crackers each
    # Calculate the number of uneaten animal crackers
    uneaten_animal_crackers = 2 * 10  # 2 students did not eat their animal crackers, each pack contains 10 animal crackers
    # Calculate the number of eaten animal crackers
    eaten_animal_crackers = total_animal_crackers - uneaten_animal_crackers
    result = eaten_animal_crackers
    return result

print(solution())