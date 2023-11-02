def solution():
    # Define the prices of each item with and without the discount
    shirt_price = 20
    shirt_discounted_price = shirt_price * 0.9
    pants_price = 80
    pants_discounted_price = pants_price * 0.9
    shoes_price = 150
    shoes_discounted_price = shoes_price * 0.9

    # Calculate the total cost of Eugene's purchase
    total_cost = (shirt_discounted_price * 4) + (pants_discounted_price * 3) + (shoes_discounted_price * 2)
    result = total_cost
    return result

print(solution())