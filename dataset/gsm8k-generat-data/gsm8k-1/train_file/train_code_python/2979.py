def solution():
    """At his craftwork store, Howard has a collection of 70 wooden bowls where he rewards two to his customers for every 10 they buy. If he had 20 customers that day, half of whom bought 20 bowls each, calculate the number of bowls remaining in the rewards collection."""
    total_bowls = 70
    bowls_given_per_10 = 2
    customers = 20
    bowls_bought_per_customer = 20
    reward_bowls_given = (bowls_bought_per_customer // 10) * bowls_given_per_10
    reward_bowls_given_total = reward_bowls_given * (customers / 2)
    bowls_remaining = total_bowls - reward_bowls_given_total
    result = bowls_remaining
    return result

print(solution())