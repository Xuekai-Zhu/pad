def solution():
    """Care and Rick have a repair shop. Each repair is priced differently: phone repair costs $11, laptop repair costs $15 and computer repair costs $18. If they perform 5 phone repairs, 2 laptop repairs, and 2 computer repairs for this week, how much did they earn for the week?"""
    # Define the price of each repair type
    PHONE_PRICE = 11
    LAPTOP_PRICE = 15
    COMPUTER_PRICE = 18

    # Define the number of repairs performed for each type
    phone_repairs = 5
    laptop_repairs = 2
    computer_repairs = 2

    # Calculate the total earnings for the week
    total_earnings = (PHONE_PRICE * phone_repairs) + (LAPTOP_PRICE * laptop_repairs) + (COMPUTER_PRICE * computer_repairs)

    # Return the total earnings
    result = total_earnings
    return result

print(solution())