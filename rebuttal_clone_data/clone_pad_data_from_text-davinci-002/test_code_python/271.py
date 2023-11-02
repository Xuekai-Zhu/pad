def solution():
     """Nadia was sent to the flower shop to buy 20 roses and 3/4 times as many Lillies as roses. If roses cost $5 each and lilies cost twice as much each, calculate the total amount of money Nadia used to buy the flowers."""
    rose_cost = 5
    lily_cost = rose_cost * 2
    roses_bought = 20
    lilies_bought = (3/4) * roses_bought
    total_cost = (roses_bought * rose_cost) + (lilies_bought * lily_cost)
    result = total_cost
    return result

print(solution())