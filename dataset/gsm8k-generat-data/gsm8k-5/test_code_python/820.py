def solution():
    # Calculate the total cost of the meal
    total_cost = 16 + 14  # James ordered a meal for $16 and his friend ordered a meal for $14

    # Calculate the tip amount
    tip = total_cost * 0.2  # They tipped 20% of the total cost

    # Calculate James' half of the bill
    james_half = (total_cost + tip) / 2

    # Calculate the total amount James paid
    james_paid = james_half + tip
    result = james_paid
    return result

print(solution())