def solution():
    # Convert tub capacity from gallons to quarts
    tub_capacity = 40 * 4

    # Calculate how many bottles of champagne are needed to fill the tub
    bottles_needed = tub_capacity / 4

    # Calculate the cost of the champagne without discount
    cost_before_discount = bottles_needed * 50

    # Calculate the volume discount
    volume_discount = 0.2 * cost_before_discount

    # Calculate the cost of the champagne after discount
    cost_after_discount = cost_before_discount - volume_discount

    result = cost_after_discount
    return result

print(solution())