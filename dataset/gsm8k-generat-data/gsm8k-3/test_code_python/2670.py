def solution():
    """At a people counting station, the number of people counted on the first day was twice the total number counted on the second day. If 500 people were counted on the second day, how many people were counted on the two days?"""
    # Define the number of people counted on the second day
    day2_count = 500

    # Calculate the number of people counted on the first day
    day1_count = day2_count * 2

    # Calculate the total number of people counted
    total_count = day1_count + day2_count

    # Display the total number of people counted
    result = total_count
    return result

print(solution())