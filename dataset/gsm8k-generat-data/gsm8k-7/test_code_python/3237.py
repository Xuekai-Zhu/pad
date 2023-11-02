def solution():
    num_pancakes_made = 12
    num_people = 8

    # Calculate the total number of pancakes needed for everyone to have a second pancake
    total_pancakes_needed = num_people * 2 - num_pancakes_made

    result = total_pancakes_needed
    return result

print(solution())