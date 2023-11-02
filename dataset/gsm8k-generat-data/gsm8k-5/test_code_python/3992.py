def solution():
    lobster_harbor1 = 80  # The first harbor has 80 pounds of lobster
    lobster_harbor2 = 80  # The second harbor has 80 pounds of lobster

    # The total amount of lobster in Hooper Bay is twice the sum of the other two harbors
    lobster_hooper_bay = 2 * (lobster_harbor1 + lobster_harbor2)

    # Calculate the total amount of lobster in all three harbors
    total_lobster = lobster_harbor1 + lobster_harbor2 + lobster_hooper_bay
    result = total_lobster
    return result

print(solution())