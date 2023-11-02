def solution():
    # Find the number of times the vending machine does not drop a snack
    no_drop = 30 * (5/6)  # the machine fails to drop a snack one in six times

    # Find the number of times the vending machine drops two snacks accidentally
    double_drop = 30 * (1/10)  # one in ten times, it will accidentally drop two snacks

    # Find the number of snacks dropped by the vending machine
    snacks_dropped = no_drop + 2*double_drop  # the rest of the time, it drops the purchased snack

    result = snacks_dropped
    return result

print(solution())