def solution():
    original_price = 4  # The original price of the Russian dolls is $4 each
    new_price = 3  # The discounted price of the Russian dolls is now $3 each
    original_count = 15  # Daniel has enough money to buy 15 Russian dolls at the original price

    # Calculate the amount of money Daniel needs for the original price
    original_cost = original_price * original_count

    # Calculate the number of Russian dolls he can buy at the discounted price
    discounted_count = original_cost // new_price

    result = discounted_count
    return result

print(solution())