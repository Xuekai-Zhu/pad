def solution():
    slices_per_tomato = 8  # Thelma cuts each tomato into 8 slices
    slices_per_meal = 20  # Thelma needs 20 slices to make a meal for one person
    people_in_family = 8  # Thelma needs to feed a family of 8

    # Calculate the total number of slices needed for the family
    total_slices_needed = slices_per_meal * people_in_family

    # Calculate the total number of tomatoes needed
    total_tomatoes_needed = total_slices_needed / slices_per_tomato
    result = total_tomatoes_needed
    return result

print(solution())