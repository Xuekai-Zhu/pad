def solution():
    num_benches = 50
    capacity_per_bench = 4
    num_people_sitting = 80

    # Calculate the total carrying capacity of all benches
    total_capacity = num_benches * capacity_per_bench

    # Calculate the number of available spaces on the benches
    available_spaces = total_capacity - num_people_sitting
    result = available_spaces
    return result

print(solution())