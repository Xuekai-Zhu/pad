def solution():
    
    # Define the number of bandages used on the first day
    bandages_day1 = 38

    # Define the number of bandages used on the second day
    bandages_day2 = bandages_day1 - 10

    # Define the number of bandages used on the third day
    bandages_day3 = bandages_day2 / 2

    # Define the number of bandages left at the end of the third day
    bandages_day3 = 78

    # Calculate the total number of bandages used
    total_bandages_used = bandages_day1 + bandages_day2 + bandages_day3

    # Calculate the number of bandages left on the first day
    bandages_day1 = total_bandages_used - bandages_day3

    # Display the number of bandages on the first day
    result = bandages_day1
    return result

print(solution())