def solution():
    
    # Define the time it takes to dry on one painting and one of the new varnish
    old_time = 7
    new_time = 12

    # Calculate the difference in time between the two paintings
    time_difference = new_time - old_time

    # Calculate the total time it takes to dry 6 paintings with the new varnish
    total_time_6_paintings = 6 * new_time

    # Display the total time it takes to dry 6 paintings with the old varnish
    result = total_time_6_paintings
    return result

print(solution())