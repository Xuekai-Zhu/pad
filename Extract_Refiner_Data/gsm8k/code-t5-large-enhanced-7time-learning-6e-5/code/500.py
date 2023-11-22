def solution():
    
    # Define the total cost of the gum
    total_cost = 7

    # Define the number of packs of each flavor of gum purchased
    grape_packs = 4
    strawberry_packs = 2

    # Define the cost of the grape gum
    grape_cost = 2

    # Define the cost of the green apple gum
    green_cost = grape_cost / 2

    # Calculate the total cost of the gum purchased
    total_purchased = grape_packs * grape_cost + strawberry_packs * strawberry_cost

    # Calculate the cost of each pack of strawberry gum
    strawberry_cost = total_cost - total_purchased
    cost_per_pack = strawberry_cost / strawberry_packs

    # Display the cost per pack of strawberry gum
    result = cost_per_pack
    return result

print(solution())