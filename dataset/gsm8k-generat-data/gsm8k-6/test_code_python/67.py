def solution():
    # Calculate the total distance each person runs in the first 4 days
    jesse_distance = (2/3)*3 + 10 # Jesse averages 2/3 of a mile for the first 3 days, then runs 10 miles on the fourth day
    mia_distance = 3*4  # Mia averages 3 miles a day for the first 4 days

    # Calculate how much distance they have left to run in the final three days
    remaining_distance = 30 - jesse_distance - mia_distance

    # Calculate the average of their average that they have to run over the final three days
    average_remaining_distance = remaining_distance / 3

    result = average_remaining_distance
    return result

print(solution())