def solution():
    """Care and Rick have a repair shop. Each repair is priced differently: phone repair costs $11, laptop repair costs $15 and computer repair costs $18. If they perform 5 phone repairs, 2 laptop repairs, and 2 computer repairs for this week, how much did they earn for the week?"""
    # Define the prices for each type of repair
    PHONE_PRICE = 11
    LAPTOP_PRICE = 15
    COMPUTER_PRICE = 18

    # Define the number of each type of repair performed this week
    num_phone_repairs = 5
    num_laptop_repairs = 2
    num_computer_repairs = 2

    # Calculate the total earnings for the week
    total_earnings = (num_phone_repairs * PHONE_PRICE) + (num_laptop_repairs * LAPTOP_PRICE) + (num_computer_repairs * COMPUTER_PRICE)

    # Display the total earnings for the week
    result = total_earnings
    return result

print(solution())