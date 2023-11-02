def solution():
    """At his craftwork store, Howard has a collection of 70 wooden bowls where he rewards two to his customers for every 10 they buy. If he had 20 customers that day, half of whom bought 20 bowls each, calculate the number of bowls remaining in the rewards collection."""
    # Define the number of wooden bowls Howard has
    total_bowls = 70

    # Calculate the number of customers who bought 20 bowls each
    customers_20bowls = 20 / 2

    # Calculate the total number of bowls bought by the customers who bought 20 bowls each
    bowls_20bowls = customers_20bowls * 20

    # Calculate the total number of wooden bowls Howard rewarded
    bowls_rewarded = (bowls_20bowls // 10) * 2

    # Calculate the number of wooden bowls remaining in the rewards collection
    bowls_remaining = total_bowls - bowls_rewarded

    # return the result
    result = bowls_remaining
    return result

print(solution())