def solution():
    
    # Define the number of hours Jen works per week and her hourly rate
    HOURS_PER_WEEK = 7.5 * 6
    HOURLY_RATE = 1.5

    # Calculate the total number of hours Jen works in April
    total_hours = HOURS_PER_WEEK * 4

    # Calculate the total amount of money Jen will receive
    total_money = total_hours * HOURLY_RATE + 10

    # Display the total amount of money Jen will receive
    result = total_money
    return result

print(solution())