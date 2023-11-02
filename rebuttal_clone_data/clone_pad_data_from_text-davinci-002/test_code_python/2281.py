def solution():
    number_of_guests = 4
    servings_per_guest = 1.5
    number_of_pancakes_per_serving = 4
    total_number_of_pancakes = (number_of_guests * servings_per_guest) * number_of_pancakes_per_serving
    result = total_number_of_pancakes
    return result

print(solution())