def solution():
    # Calculate the total cost of Andy's snacks
    andy_total_cost = 1 + 2 * 2  # Andy bought a can of soda for $1 and two hamburgers for $2 each

    # Calculate the total cost of Bob's snacks
    bob_total_cost = 2 * 3 + x  # Bob bought two sandwiches for $3 each and a can of fruit drink for x dollars

    # Since they spent the same amount, set the two total costs equal to each other
    # and solve for x, the cost of Bob's fruit drink
    x = (andy_total_cost - bob_total_cost) * -1

    result = x
    return result

print(solution())