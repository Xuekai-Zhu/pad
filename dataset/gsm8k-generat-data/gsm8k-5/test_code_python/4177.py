def solution():
    # Let x be the weight of the chihuahua
    x = 1
    # The pitbull weighs 3 times as much as the chihuahua
    y = 3 * x
    # The great dane weighs 10 more pounds than triple the pitbull
    z = 3 * y + 10
    # The combined weight of the three dogs is 439 pounds
    total_weight = x + y + z
    
    # The great dane's weight is z
    result = z
    return result

print(solution())