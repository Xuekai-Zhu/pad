def solution():
    num_shirts = 4
    shirt_price = 8

    num_pants = 2
    pants_price = 18

    num_jackets = 2
    jacket_price = 60

    # Calculate the total cost of all shirts
    total_shirts_cost = num_shirts * shirt_price

    # Calculate the total cost of all pants
    total_pants_cost = num_pants * pants_price

    # Calculate the total cost of all jackets
    total_jackets_cost = num_jackets * jacket_price

    # Calculate the total cost of all clothing items
    total_cost = total_shirts_cost + total_pants_cost + total_jackets_cost

    # Calculate Carrie's payment
    carrie_payment = total_cost / 2
    result = carrie_payment
    return result

print(solution())