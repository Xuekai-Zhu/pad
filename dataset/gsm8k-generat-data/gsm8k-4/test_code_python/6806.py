def solution():
    """Daniel collects Russian dolls that normally cost $4 each. He saves enough money to buy 15 Russian dolls. However, the price suddenly drops to $3 each. How many Russian dolls can he buy now at the discounted price, given his savings?"""
    # Define the original price per Russian doll and the number of dolls Daniel can buy
    original_price = 4
    num_dolls = 15

    # Calculate the amount of money Daniel has saved
    savings = original_price * num_dolls

    # Calculate the new price per Russian doll and the number of dolls Daniel can buy at the discounted price
    discounted_price = 3
    num_discounted_dolls = savings // discounted_price

    # Return the result
    result = int(num_discounted_dolls)
    return result

print(solution())