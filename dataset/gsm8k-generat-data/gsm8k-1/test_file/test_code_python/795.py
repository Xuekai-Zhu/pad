def solution():
    """A loaf of bread at the bakery costs $2. Bagels cost $1 each. How much more do 3 loaves of bread cost than 2 bagels?"""
    bread_cost = 2
    bagel_cost = 1
    num_bread = 3
    num_bagels = 2
    total_bread_cost = bread_cost * num_bread
    total_bagel_cost = bagel_cost * num_bagels
    difference = total_bread_cost - total_bagel_cost
    result = difference
    return result

print(solution())