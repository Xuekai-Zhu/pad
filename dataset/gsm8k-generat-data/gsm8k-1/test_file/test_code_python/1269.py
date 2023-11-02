def solution():
    """Mazie has 52 marbles and gives them to twins, Dallas and Darla. If Dallas has a total of 21 marbles after dropping 4 of them in the playground, how many did Mazie give to Darla?"""
    total_marbles = 52
    dallas_marbles = 21 + 4
    darla_marbles = total_marbles - dallas_marbles
    result = darla_marbles
    return result

print(solution())