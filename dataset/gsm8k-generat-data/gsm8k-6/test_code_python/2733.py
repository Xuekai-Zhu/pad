def solution():
    # Calculate the number of ducks after 5 years
    ducks_after_5_years = (100 - 20 + 30) * 5  # every year 20 ducks are killed but 30 are born
    total_ducks = ducks_after_5_years + 150  # combined flock size after 5 years
    result = total_ducks
    return result

print(solution())