def solution():
    """Surfers enjoy going to the Rip Curl Myrtle Beach Surf Festival. There were 1500 surfers at the Festival on the first day, 600 more surfers on the second day than the first day, and 2/5 as many surfers on the third day as the first day. What is the average number of surfers at the Festival for the three days?"""
    # Define the number of surfers on each day
    surfers_day1 = 1500
    surfers_day2 = surfers_day1 + 600
    surfers_day3 = surfers_day1 * 2/5

    # Calculate the total number of surfers over the three days
    total_surfers = surfers_day1 + surfers_day2 + surfers_day3

    # Calculate the average number of surfers over the three days
    avg_surfers = total_surfers / 3

    result = avg_surfers
    return result

print(solution())