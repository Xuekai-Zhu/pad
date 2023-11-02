def solution():
    """Mr. Rocky went to the market to sell his handmade crafts on a particular week. He was selling jewelry at $30 each and paintings at $100 each. However, he realized the income from the sales wasn't worth the labor and materials he had used, so he decided to increase the price of jewelry by $10 each and the cost of each painting by 20%. Calculate the total price a buyer who takes two pieces of jewelry and five paintings would pay"""
    # Define the initial prices of jewelry and paintings
    jewelry_price = 30
    painting_price = 100

    # Increase the prices based on Mr. Rocky's decision
    jewelry_price += 10
    painting_price *= 1.2

    # Calculate the total price for two pieces of jewelry and five paintings
    total_price = (2 * jewelry_price) + (5 * painting_price)

    # return the result
    result = total_price
    return result

print(solution())