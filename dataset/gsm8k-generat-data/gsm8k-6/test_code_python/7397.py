def solution():
    # Calculate the amount of money that Ryan needs to raise
    target_amount = 1000 - 200  # Ryan already has $200
    # Calculate the number of people Ryan needs to recruit to reach his funding goal
    num_people = target_amount / 10  # Assuming each person funds $10
    result = num_people
    return result

print(solution())