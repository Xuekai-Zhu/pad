def solution():
    """Nadia was sent to the flower shop to buy 20 roses and 3/4 times as many Lillies as roses. If roses cost $5 each and lilies cost twice as much each, calculate the total amount of money Nadia used to buy the flowers."""
    num_roses = 20
    num_lilies = int(3/4 * num_roses)
    rose_cost = 5
    lily_cost = 2 * rose_cost
    total_cost = num_roses * rose_cost + num_lilies * lily_cost
    result = total_cost
    return result

print(solution())