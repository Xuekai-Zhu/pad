def solution():
    # Define the variables
    total_apples = 64
    num_baskets = 4
    apples_per_basket = total_apples / num_baskets
    apples_per_basket_after_theft = apples_per_basket - 3

    # Calculate the number of apples per basket after the theft
    result = apples_per_basket_after_theft
    return result

print(solution())