def solution():
    num_sandwiches = 20  # Donna makes 20 sandwiches
    portions_per_sandwich = 4  # Each sandwich is cut into 4 portions
    total_portions = num_sandwiches * portions_per_sandwich  # Total number of portions

    # Calculate the number of people that can be fed
    num_people = total_portions // 8
    result = num_people
    return result

print(solution())