def solution():
    chocolate_cake_price = 12
    num_chocolate_cakes = 3

    strawberry_cake_price = 22
    num_strawberry_cakes = 6

    # Calculate the total cost of all chocolate cakes
    total_chocolate_cake_cost = chocolate_cake_price * num_chocolate_cakes

    # Calculate the total cost of all strawberry cakes
    total_strawberry_cake_cost = strawberry_cake_price * num_strawberry_cakes

    # Calculate the total cost of all cakes
    total_cost = total_chocolate_cake_cost + total_strawberry_cake_cost
    result = total_cost
    return result

print(solution())