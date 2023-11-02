def solution():
    """A chihuahua, pitbull, and great dane weigh a combined weight of 439 pounds. The pitbull weighs 3 times as much as the chihuahua. The great dane weighs 10 more pounds than triple the pitbull. How much does the great dane weigh?"""
    # Define the weight of the chihuahua as x
    x = 0

    # Define the weight of the pitbull as three times the weight of the chihuahua
    pitbull_weight = 3 * x

    # Calculate the weight of the great dane as 10 more than triple the weight of the pitbull
    greatdane_weight = (3 * pitbull_weight) + 10

    # Calculate the total weight of the three dogs
    total_weight = x + pitbull_weight + greatdane_weight

    # Use the total weight to solve for x and calculate the weight of the great dane
    x = (439 - 10) / 10
    greatdane_weight = (3 * (3 * x)) + 10

    result = greatdane_weight
    return result

print(solution())