def solution():
    """Jim decides he wants to practice for a marathon coming up. He starts off by running 5 miles every day for 30 days straight. He then pushes himself to run 10 miles a day for the next 30 days. Finally, as marathon day gets closer Jim runs 20 miles a day for 30 days straight. How many miles does Jim run in total during the 90 days?"""
    # Define the number of days for each running period
    period_1_days = 30
    period_2_days = 30
    period_3_days = 30

    # Define the distances for each running period
    period_1_distance = 5
    period_2_distance = 10
    period_3_distance = 20

    # Calculate the total distance run during each period
    period_1_total = period_1_days * period_1_distance
    period_2_total = period_2_days * period_2_distance
    period_3_total = period_3_days * period_3_distance

    # Calculate the total distance run during the 90 days
    total_distance = period_1_total + period_2_total + period_3_total

    # Return the result
    result = total_distance
    return result

print(solution())