def solution():
    eggs_per_plate = 2  # Each breakfast plate has 2 eggs
    bacon_per_plate = 2 * eggs_per_plate  # Each breakfast plate has twice as many bacon strips as eggs
    num_plates = 14  # 14 customers order breakfast plates

    # Calculate the total number of bacon strips needed
    total_bacon = bacon_per_plate * num_plates
    result = total_bacon
    return result

print(solution())