def solution():
    erika_siblings = 3
    friends = 3
    lost_chalk = 2
    extra_chalk = 12
    chalk_per_person = 3

    # Calculate the total number of people drawing
    total_people = erika_siblings + friends

    # Calculate the total number of pieces of chalk needed for everyone
    total_chalk_needed = total_people * chalk_per_person

    # Calculate the number of pieces of chalk lost
    lost_total = lost_chalk * (erika_siblings + 1)
    # Add extra chalk and lost chalk to original amount to get the total number of chalk
    total_chalk = total_chalk_needed + extra_chalk - lost_total

    result = total_chalk
    return result

print(solution())