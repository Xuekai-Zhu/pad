def solution():
    total_people = 1 + 1 + 1 + 1 + 1 + 1 + 4 + 2 + 2 + 2 + 2 + 3  # Total number of people in Matt's family and Uncle Joe's family
    total_sleeping_capacity = 4  # The house only sleeps 4 people

    # Calculate the number of people who need to sleep outside
    people_sleeping_outside = total_people - total_sleeping_capacity

    # Calculate the number of tents needed
    tents_needed = people_sleeping_outside / 2

    result = tents_needed
    return result

print(solution())