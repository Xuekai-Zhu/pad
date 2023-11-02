def solution():
    # Define the variables
    num_puppies = 8
    given_away = num_puppies // 2
    remaining = num_puppies - given_away
    kept = 1
    sold = remaining - kept
    sale_price = 600
    stud_fee = 300

    # Calculate the profit
    total_sale = sold * sale_price
    total_profit = total_sale - stud_fee

    result = total_profit
    return result

print(solution())