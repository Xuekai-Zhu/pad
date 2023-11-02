def solution():
    
    # Define the initial amount of money
    initial_money = 18

    # Add $5 to the eldest's share
    eldest_money += 5

    # Add $10 to the second day
    second_day_money += 10

    # Add $8 to the third day
    second_day_money += 8

    # Triple the amount he had left after spending the $8
    remaining_money = initial_money - second_day_money

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())