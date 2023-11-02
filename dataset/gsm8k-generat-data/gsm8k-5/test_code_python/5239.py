def solution():
    total_peanuts = 4 * 30  # Uncle Lou has 4 bags of peanuts, with 30 peanuts in each bag
    total_time = 120  # Uncle Lou's flight is 2 hours long

    # Calculate the interval time between eating each peanut
    interval_time = total_time / (total_peanuts - 1)
    interval_time_minutes = interval_time * 60  # Convert the interval time to minutes
    result = interval_time_minutes
    return result

print(solution())