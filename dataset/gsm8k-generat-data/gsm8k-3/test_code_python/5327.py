def solution():
    """Mr. Rocky went to the market to sell his handmade crafts on a particular week. He was selling jewelry at $30 each and paintings at $100 each. However, he realized the income from the sales wasn't worth the labor and materials he had used, so he decided to increase the price of jewelry by $10 each and the cost of each painting by 20%. Calculate the total price a buyer who takes two pieces of jewelry and five paintings would pay"""
    
    # Define the original prices
    jewelry_price = 30
    painting_price = 100
    
    # Define the new prices
    new_jewelry_price = 40
    new_painting_price = painting_price + (painting_price * 0.2)
    
    # Define the number of jewelry and paintings bought
    jewelry_bought = 2
    paintings_bought = 5
    
    # Calculate the total cost
    total_cost = (jewelry_bought * new_jewelry_price) + (paintings_bought * new_painting_price)
    
    # Display the total cost
    result = total_cost
    return result

print(solution())