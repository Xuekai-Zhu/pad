def solution():
    """Sheena is sewing the bridesmaid’s dresses for her sister’s wedding. She can sew one dress in 12 hours. There are 5 bridesmaids in the wedding. If Sheena sews the dresses 4 hours each week, how many weeks will it take her to complete them?"""
    # Define the time it takes to sew one dress
    TIME_PER_DRESS = 12

    # Define the number of bridesmaids and calculate the total number of dresses
    num_bridesmaids = 5
    total_dresses = num_bridesmaids

    # Calculate the total time it will take to sew all the dresses
    total_time = total_dresses * TIME_PER_DRESS

    # Calculate the number of weeks it will take Sheena to complete the dresses
    weeks = total_time / 4

    # Round up to the nearest week
    import math
    weeks = math.ceil(weeks)

    # Display the number of weeks
    result = weeks
    return result

print(solution())