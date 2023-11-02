def solution():
    """Mr. Zubir bought a pair of pants, a shirt, and a coat. The pair of pants and shirt costs $100. The pants and coat cost $244. The coat costs 5 times as much as the shirt. How much did Mr. Zubir pay for his coat?"""
    # Let's use variables to represent unknown values
    shirt_price = x
    coat_price = 5 * shirt_price
    pants_price = 100 - shirt_price  # We know the total cost of pants and shirt is $100, so we can solve for pants price
    
    # We also know the total cost of pants and coat is $244
    # Using our variables, we can create an equation: pants_price + coat_price = $244
    # Substituting our expressions for pants_price and coat_price, we get:
    (100 - shirt_price) + 5 * shirt_price = 244
    
    # Solving for shirt_price:
    4 * shirt_price = 144
    shirt_price = 36
    
    # Now we can find the coat price using our expression from earlier:
    coat_price = 5 * shirt_price
    result = coat_price
    
    return result

print(solution())