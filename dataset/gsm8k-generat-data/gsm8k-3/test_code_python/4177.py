def solution():
    """A chihuahua, pitbull, and great dane weigh a combined weight of 439 pounds. The pitbull weighs 3 times as much as the chihuahua.  The great dane weighs 10 more pounds than triple the pitbull.  How much does the great dane weigh?"""
    # Define the weight of the chihuahua
    chihuahua_weight = 0

    # Calculate the weight of the pitbull
    pitbull_weight = 3 * chihuahua_weight

    # Calculate the weight of the great dane
    great_dane_weight = 3 * pitbull_weight + 10

    # Calculate the total weight of all three dogs
    total_weight = chihuahua_weight + pitbull_weight + great_dane_weight

    # Display the weight of the great dane
    result = great_dane_weight
    return result

print(solution())