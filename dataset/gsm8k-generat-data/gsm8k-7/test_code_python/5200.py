def solution():
    num_tshirts = 5
    tshirt_price = 100

    total_paid = 1500

    # Calculate the total cost of all t-shirts
    total_tshirt_cost = num_tshirts * tshirt_price

    # Calculate the cost of all pants
    pants_cost = total_paid - total_tshirt_cost

    # Calculate the cost per pair of pants
    pants_price = pants_cost / 4
    result = pants_price
    return result

print(solution())