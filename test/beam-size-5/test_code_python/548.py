def solution():
    
    # Define the prices of goods and commission rate
    good_price = 1000
    commission_rate = 0.3

    # Calculate the commission earned by selling goods
    good_commission = good_price * commission_rate

    # Calculate the total earnings from selling goods
    good_earnings = good_price - good_commission

    # Calculate the additional commission earned by Sales over $1000
    additional_commission = 0.1 * good_commission_rate

    # Calculate the total earnings
    total_earnings = good_earnings + additional_commission

    # Display the total earnings
    result = total_earnings
    return result

print(solution())