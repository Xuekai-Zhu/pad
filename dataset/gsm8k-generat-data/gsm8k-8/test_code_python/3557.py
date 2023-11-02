def solution():
    # Convert pool capacity to milliliters
    pool_capacity = 2000 * 1000

    # Calculate the amount of water that can be in the pool before Jim has to refill it
    refill_capacity = 0.8 * pool_capacity

    # Calculate the amount of water that splashes out with each jump
    splash_amount = 400

    # Calculate the number of jumps before the pool needs to be refilled
    jumps_before_refill = int(refill_capacity / splash_amount)

    result = jumps_before_refill
    return result

print(solution())