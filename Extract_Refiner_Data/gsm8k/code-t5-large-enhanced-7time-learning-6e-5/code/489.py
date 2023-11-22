def solution():
    
    # Define the cost of one pack of razors and the discounted cost of one pack
    PACK_PRICE = 4.00
    DISCOUNTED_PRICE = PACK_PRICE - 2.00

    # Define the number of packs of razors purchased
    packs_purchased = 2

    # Calculate the cost of the razors purchased
    total_cost = packs_purchased * PACK_PRICE

    # Calculate the cost per razor after the discount
    cost_per_rabor = total_cost / (packs_purchased + 1)

    # Display the cost per razor
    result = cost_per_rabor
    return result

print(solution())