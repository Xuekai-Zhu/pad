def solution():
    """A chihuahua, pitbull, and great dane weigh a combined weight of 439 pounds. The pitbull weighs 3 times as much as the chihuahua. The great dane weighs 10 more pounds than triple the pitbull. How much does the great dane weigh?"""
    total_weight = 439
    pitbull_weight = 3 * chihuahua_weight
    great_dane_weight = (3 * pitbull_weight) + 10
    sum_weight = chihuahua_weight + pitbull_weight + great_dane_weight
    result = great_dane_weight
    return result

print(solution())