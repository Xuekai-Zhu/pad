def solution():
    apple_price = 1
    orange_price = 2
    banana_price = 3
    num_apples = 5
    num_oranges = 3
    num_bananas = 2

    # Calculate the total cost for each type of fruit
    total_apple_cost = num_apples * apple_price
    total_orange_cost = num_oranges * orange_price
    total_banana_cost = num_bananas * banana_price

    # Calculate the total cost of all fruits
    total_cost = total_apple_cost + total_orange_cost + total_banana_cost

    # Calculate the number of discounts Mary is eligible for
    num_discounts = (num_apples + num_oranges + num_bananas) // 5

    # Calculate the total discount amount
    discount_amount = num_discounts * 1

    # Calculate the final amount Mary will pay
    final_amount = total_cost - discount_amount
    result = final_amount
    return result

print(solution())