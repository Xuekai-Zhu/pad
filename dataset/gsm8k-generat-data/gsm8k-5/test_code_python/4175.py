def solution():
    total_purchases = 30  # 30 people have used the vending machine once each

    # Calculate the number of times the vending machine fails to drop a snack
    no_snack = total_purchases // 6

    # Calculate the number of times the vending machine accidentally drops two snacks
    two_snacks = total_purchases // 10

    # Calculate the number of snacks dropped by the vending machine
    snacks_dropped = total_purchases - no_snack - two_snacks

    result = snacks_dropped
    return result

print(solution())