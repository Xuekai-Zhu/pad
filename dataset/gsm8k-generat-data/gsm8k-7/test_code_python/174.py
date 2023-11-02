def solution():
    monday_price = 5
    wednesday_price = 2 * monday_price
    saturday_price = 5 * monday_price

    # Glenn goes to the movie theater on Wednesday and Saturday
    total_cost = wednesday_price + saturday_price
    result = total_cost
    return result

print(solution())