def solution():
    """There are four times as many boys at Lulu's party as girls. Each boy paid twice the money that each girl paid to attend the party.
    If there are 40 boys at the party and each boy paid $50 to attend the party, calculate the total amount of money collected at the party."""
    # Calculate the number of girls
    girls = 40 / 4

    # Calculate the amount paid by each girl
    girl_cost = 50 / 2

    # Calculate the total amount paid by the girls
    girls_total = girls * girl_cost

    # Calculate the total amount paid by the boys
    boys_total = 40 * 50

    # Calculate the total amount collected at the party
    total = girls_total + boys_total

    result = total
    return result

print(solution())