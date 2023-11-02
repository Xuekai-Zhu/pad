def solution():
    total_capacity = 50 * 4  # The total capacity of the benches in the park
    occupied_spaces = 80  # The number of people sitting on the benches

    # Calculate the number of available spaces on the benches
    available_spaces = total_capacity - occupied_spaces
    result = available_spaces
    return result

print(solution())