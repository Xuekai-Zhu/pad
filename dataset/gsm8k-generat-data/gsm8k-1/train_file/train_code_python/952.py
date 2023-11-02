def solution():
    """Wendi brought home 4 chickens. After a few days, she brought home enough additional chickens to double the number of chickens she owned. Then, a neighbor's dog ate one of her chickens. Finally, Wendi found an additional 4 less than ten chickens and brought them home too. After this, how many chickens does Wendi have?"""
    initial_chickens = 4
    additional_chickens = initial_chickens * 2
    lost_chickens = 1
    found_chickens = 10 - 4
    total_chickens = initial_chickens + additional_chickens + found_chickens - lost_chickens
    result = total_chickens
    return result

print(solution())