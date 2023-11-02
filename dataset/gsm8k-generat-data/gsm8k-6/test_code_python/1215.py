def solution():
    # Calculate the total number of servings needed
    num_people = 6  # Brian, his wife, his 2 kids, his parents, and his wife's parents
    servings_per_person = 2
    total_servings = num_people * servings_per_person

    # Calculate the total amount of milk needed
    milk_per_serving = 0.5  # in US cups
    milk_total = total_servings * milk_per_serving * 250  # in ml

    # Calculate the number of 1L cartons of milk needed
    cartons_of_milk = milk_total // 1000 + 1  # round up to the nearest carton
    result = cartons_of_milk
    return result

print(solution())