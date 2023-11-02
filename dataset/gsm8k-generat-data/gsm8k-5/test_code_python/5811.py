def solution():
    # Calculate the total amount earned in September
    money_september = (4 * 25) + (8 * 3)  # $4 per hour for 25 hours of mowing and $8 per hour for 3 hours of weeding

    # Calculate the total amount earned in October assuming she worked the same number of hours
    money_october = (4 * 25) + (8 * 3)  # $4 per hour for 25 hours of mowing and $8 per hour for 3 hours of weeding

    # Calculate the total amount earned in September and October
    total_money = money_september + money_october
    result = total_money
    return result

print(solution())