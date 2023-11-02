def solution():
    cards_per_box = 6
    box1_price = 1.25
    box2_price = 1.75

    # Calculate the total cost of cards from box 1
    box1_cost = cards_per_box * box1_price

    # Calculate the total cost of cards from box 2
    box2_cost = cards_per_box * box2_price

    # Calculate the total cost of all cards
    total_cost = box1_cost + box2_cost
    result = total_cost
    return result

print(solution())