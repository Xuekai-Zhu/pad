def solution():
    
    # Define the initial number of bananas
    initial_bananas = 48

    # Calculate the number of bananas stolen on the first day
    day1_bananas = initial_bananas / 2

    # Calculate the number of bananas stolen on the second day
    day2_bananas = day1_bananas + 25

    # Calculate the number of bananas stolen on the third day
    day3_bananas = 6

    # Calculate the total number of bananas added
    total_bananas = day1_bananas + day2_bananas + day3_bananas

    # Display the total number of bananas
    result = total_bananas
    return result

print(solution())