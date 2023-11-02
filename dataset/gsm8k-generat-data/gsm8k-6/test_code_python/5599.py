def solution():
    # Calculate the distance Mairead walked and jogged
    miles_ran = 40
    miles_walked = (3/5) * miles_ran
    miles_jogged = miles_walked / 5

    # Calculate the total distance Mairead covered
    total_distance = miles_ran + miles_walked + miles_jogged
    result = total_distance
    return result

print(solution())