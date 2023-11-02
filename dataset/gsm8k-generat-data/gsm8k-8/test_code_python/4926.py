def solution():
    # Calculate the total number of carrots planted
    total_carrots_planted = 400 * 300

    # Calculate the number of carrots planted per hour
    carrots_per_hour = total_carrots_planted / 20

    result = int(carrots_per_hour)
    return result

print(solution())