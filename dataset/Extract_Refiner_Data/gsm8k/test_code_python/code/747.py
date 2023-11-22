def solution():
    
    # Define the initial number of bananas
    initial_bananas = 48

    # Calculate the number of bananas stole by Arnold on the first day
    arnold_day1 = initial_bananas / 2

    # Calculate the number of bananas stole by Arnold on the second day
    arnold_day2 = arnold_day1 + 12

    # Calculate the number of bananas added on the third day
    gunther_day3 = gunther_day2 + 6

    # Calculate the total number of bananas
    total_bananas = initial_bananas + arnold_day1 + arnold_day2 + gunther_day3

    # Display the total number of bananas
    result = total_bananas
    return result

print(solution())