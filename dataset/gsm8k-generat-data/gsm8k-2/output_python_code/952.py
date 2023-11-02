def solution():
    """Wendi brought home 4 chickens. After a few days, she brought home enough additional chickens to double the number of chickens she owned. Then, a neighbor's dog ate one of her chickens. Finally, Wendi found an additional 4 less than ten chickens and brought them home too. After this, how many chickens does Wendi have?"""
    initial_chickens = 4
    doubled_chickens = initial_chickens * 2
    dog_eaten = 1
    additional_chickens = 10 - 4
    total_chickens = initial_chickens + doubled_chickens - dog_eaten + additional_chickens
    result = total_chickens
    return result

print(solution())