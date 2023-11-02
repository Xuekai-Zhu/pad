def solution():
    # Calculate the number of actual sheep by subtracting the double-counted ones
    actual_sheep = 7

    # Add the actual number of sheep and count the pigs
    actual_animals = actual_sheep + 3

    # Calculate the total number of animals by dividing Mary's count by the ratio of actual to counted animals
    counted_animals = 60
    actual_to_counted_ratio = actual_animals / (counted_animals - 7)
    total_animals = actual_to_counted_ratio * counted_animals
    result = total_animals
    return result

print(solution())