def solution():
    total_food = 300 * 90  # Enough food for 300 people for 90 days
    remaining_food = total_food - (300 * 30)  # Food remaining after 30 days

    # Calculate the new number of people based on those who left the castle
    new_people = 300 - 100

    # Calculate how long the remaining food will last for the new number of people
    remaining_days = remaining_food / (new_people * 3)

    result = remaining_days
    return result

print(solution())