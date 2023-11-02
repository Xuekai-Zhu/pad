def solution():
    chocolate_price = 12  # Price per chocolate cake is $12
    strawberry_price = 22  # Price per strawberry cake is $22
    num_chocolate_cakes = 3  # Leila ordered 3 chocolate cakes
    num_strawberry_cakes = 6  # Leila ordered 6 strawberry cakes

    # Calculate the total cost for chocolate cakes and strawberry cakes separately
    cost_chocolate = chocolate_price * num_chocolate_cakes
    cost_strawberry = strawberry_price * num_strawberry_cakes

    # Calculate the total cost for all cakes
    total_cost = cost_chocolate + cost_strawberry
    result = total_cost
    return result

print(solution())