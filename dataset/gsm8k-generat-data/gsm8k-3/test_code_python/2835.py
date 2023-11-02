def solution():
    """Surfers enjoy going to the Rip Curl Myrtle Beach Surf Festival. There were 1500 surfers at the Festival on the first day, 600 more surfers on the second day than the first day, and 2/5 as many surfers on the third day as the first day. What is the average number of surfers at the Festival for the three days?"""
    # Define the number of surfers on the first day
    day1_surfers = 1500

    # Calculate the number of surfers on the second day
    day2_surfers = day1_surfers + 600

    # Calculate the number of surfers on the third day
    day3_surfers = day1_surfers * 2/5

    # Calculate the total number of surfers over the three days
    total_surfers = day1_surfers + day2_surfers + day3_surfers

    # Calculate the average number of surfers per day
    avg_surfers = total_surfers / 3

    # Display the average number of surfers
    result = avg_surfers
    return result

print(solution())