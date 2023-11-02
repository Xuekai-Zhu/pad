def solution():
    """Peter has to walk 2.5 miles to get to the grocery store. If it takes him 20 minutes to walk one mile and he has walked 1 mile already, how many more minutes does he have to walk to reach it?"""
    miles_left = 2.5 - 1
    time_per_mile = 20
    total_time = miles_left * time_per_mile
    result = total_time
    return result

print(solution())