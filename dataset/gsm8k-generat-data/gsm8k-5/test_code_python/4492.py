def solution():
    skirt_cost = 13  # Cost of one skirt
    blouse_cost = 6  # Cost of one blouse
    num_skirts = 2  # Number of skirts purchased
    num_blouses = 3  # Number of blouses purchased
    total_cost = (skirt_cost * num_skirts) + (blouse_cost * num_blouses)  # Total cost of purchase
    paid_amount = 100  # Amount paid by Jane
    change = paid_amount - total_cost  # Change received by Jane
    result = change
    return result

print(solution())