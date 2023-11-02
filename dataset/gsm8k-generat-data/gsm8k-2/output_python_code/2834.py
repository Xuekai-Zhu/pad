def solution():
    """Surfers enjoy going to the Rip Curl Myrtle Beach Surf Festival. There were 1500 surfers at the Festival on the first day, 600 more surfers on the second day than the first day, and 2/5 as many surfers on the third day as the first day. What is the average number of surfers at the Festival for the three days?"""
    first_day_surfers = 1500
    second_day_surfers = first_day_surfers + 600
    third_day_surfers = (2/5) * first_day_surfers
    total_surfers = first_day_surfers + second_day_surfers + third_day_surfers
    average_surfers = total_surfers / 3
    result = average_surfers
    return result

print(solution())