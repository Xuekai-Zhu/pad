def solution():
    """Mr. Rocky went to the market to sell his handmade crafts on a particular week. He was selling jewelry at $30 each and paintings at $100 each. However, he realized the income from the sales wasn't worth the labor and materials he had used, so he decided to increase the price of jewelry by $10 each and the cost of each painting by 20%. Calculate the total price a buyer who takes two pieces of jewelry and five paintings would pay."""
    jewelry_initial_price = 30
    painting_initial_price = 100
    jewelry_new_price = jewelry_initial_price + 10
    painting_new_price = painting_initial_price * 1.2
    total_price = (2 * jewelry_new_price) + (5 * painting_new_price)
    result = total_price
    return result

print(solution())