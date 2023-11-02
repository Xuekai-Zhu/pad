def solution():
    pumpkin_cost = 2.5  # Cost of a packet of pumpkin seeds
    tomato_cost = 1.5  # Cost of a packet of tomato seeds
    chili_cost = 0.9  # Cost of a packet of chili pepper seeds
    pumpkin_amount = 3  # Harry wants to buy 3 packets of pumpkin seeds
    tomato_amount = 4  # Harry wants to buy 4 packets of tomato seeds
    chili_amount = 5  # Harry wants to buy 5 packets of chili pepper seeds

    # Calculate the total cost of the seeds
    total_cost = (pumpkin_amount * pumpkin_cost) + (tomato_amount * tomato_cost) + (chili_amount * chili_cost)
    result = total_cost
    return result

print(solution())