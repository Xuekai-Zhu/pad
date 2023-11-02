def solution():
    """At his craftwork store, Howard has a collection of 70 wooden bowls where he rewards two to his customers for every 10 they buy. If he had 20 customers that day, half of whom bought 20 bowls each, calculate the number of bowls remaining in the rewards collection."""
    total_bowls = 70
    bowls_given = 2 * (sum([20 for i in range(10)]) // 10)
    remaining_bowls = total_bowls - bowls_given
    result = remaining_bowls
    return result

print(solution())