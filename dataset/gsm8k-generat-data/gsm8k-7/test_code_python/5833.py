def solution():
    shirt_price = 5
    num_shirts = 3
    jeans_price = 10
    num_jeans = 2
    hat_price = 4
    num_hats = 4

    # Calculate the total cost of all shirts
    total_shirts_cost = shirt_price * num_shirts

    # Calculate the total cost of all jeans
    total_jeans_cost = jeans_price * num_jeans

    # Calculate the total cost of all hats
    total_hats_cost = hat_price * num_hats

    # Calculate the total cost of all clothing items
    total_cost = total_shirts_cost + total_jeans_cost + total_hats_cost
    result = total_cost
    return result

print(solution())