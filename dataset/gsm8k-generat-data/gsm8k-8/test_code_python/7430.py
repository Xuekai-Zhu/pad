def solution():
    # Calculate the total carrying capacity of the benches
    total_capacity = 50 * 4

    # Calculate the number of people currently seated on the benches
    current_people = 80

    # Calculate the number of available spaces on the benches
    available_spaces = total_capacity - current_people
    result = available_spaces
    return result

print(solution())