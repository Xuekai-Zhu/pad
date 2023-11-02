def solution():
    bacon_packs = 5
    bacon_price = 10

    chicken_packs = 6
    chicken_price = bacon_price * 2

    strawberry_packs = 3
    strawberry_price = 4

    apple_packs = 7
    apple_price = strawberry_packs / 2

    total_budget = 65

    # Calculate the total cost of all bacon packs
    total_bacon_cost = bacon_packs * bacon_price

    # Calculate the total cost of all chicken packs
    total_chicken_cost = chicken_packs * chicken_price

    # Calculate the total cost of all strawberries
    total_strawberry_cost = strawberry_packs * strawberry_price

    # Calculate the total cost of all items
    total_cost = total_bacon_cost + total_chicken_cost + total_strawberry_cost + total

print(solution())