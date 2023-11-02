def solution():
    # Define Lisa's savings and the amount her mother gave her
    lisa_savings = 1200
    mother_contribution = 3/5 * lisa_savings

    # Calculate the amount Lisa's brother gave her
    brother_contribution = 2 * mother_contribution

    # Calculate the total amount of money Lisa has
    total_money = lisa_savings + mother_contribution + brother_contribution - 400

    # Calculate the price of the gift Lisa wanted to buy
    gift_price = total_money
    result = gift_price
    return result

print(solution())