def solution():
    """Liz sold her car at 80% of what she originally paid. She uses the proceeds of that sale and needs only $4,000 to buy herself a new $30,000 car. How much cheaper is her new car versus what she originally paid for her old one?"""
    # Assume Liz originally paid $x for her old car
    # She sold it at 80% of that price, so she received $0.8x for it
    # She needs $4000 more to buy the new car, so she has $30000 - $4000 = $26000 to spend
    # We want to find how much cheaper her new car is compared to her old one, so we need to subtract the cost of her new car from the cost of her old one
    # The cost of her old car is $x and the cost of her new car is $26000 + $0.8x
    # Therefore, the difference between the costs is $x - ($26000 + $0.8x) = $0.2x - $26000
    # Simplifying this expression, we get -0.2x - $26000

    # Since we don't know the value of x, we can't compute the exact value of the difference between the costs
    # However, we can see that this expression is negative, which means the new car is less expensive than the old one
    # Specifically, the new car is $26000 + 80% of the old car's price cheaper than the old car

    result = "$26000 + 80% of the old car's price cheaper than the old car"
    return result

print(solution())