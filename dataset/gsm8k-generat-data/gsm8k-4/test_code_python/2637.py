def solution():
    """Sheena is sewing the bridesmaid’s dresses for her sister’s wedding. She can sew one dress in 12 hours. There are 5 bridesmaids in the wedding. If Sheena sews the dresses 4 hours each week, how many weeks will it take her to complete them?"""
    # Define the time it takes to sew one dress
    time_per_dress = 12

    # Define the number of dresses needed
    num_dresses = 5

    # Calculate the total time needed to sew all the dresses
    total_time = time_per_dress * num_dresses

    # Calculate the number of weeks needed to complete all the dresses
    weeks_needed = total_time / 4

    # Round up to the nearest whole week
    weeks_needed = math.ceil(weeks_needed)

    result = weeks_needed
    return result

print(solution())