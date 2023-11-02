def solution():
    """There are four times as many boys at Lulu's party as girls. Each boy paid twice the money that each girl paid to attend the party. If there are 40 boys at the party and each boy paid $50 to attend the party, calculate the total amount of money collected at the party."""
    boys = 40
    girls = boys / 4
    boy_cost = 50
    girl_cost = boy_cost / 2
    total_cost = (boys * boy_cost) + (girls * girl_cost)
    result = total_cost
    return result

print(solution())