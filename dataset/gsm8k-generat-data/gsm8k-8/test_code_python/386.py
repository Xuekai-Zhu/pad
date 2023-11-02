def solution():
    # Define the original prices of shoes and dress
    shoes_price = 50
    dress_price = 100

    # Calculate the discounted prices with the sale
    shoes_discount = 0.4 * shoes_price
    dress_discount = 0.2 * dress_price
    discounted_shoes_price = shoes_price - shoes_discount
    discounted_dress_price = dress_price - dress_discount

    # Calculate the total cost of Daniela's purchase
    total_cost = 2 * discounted_shoes_price + discounted_dress_price
    result = total_cost
    return result

print(solution())