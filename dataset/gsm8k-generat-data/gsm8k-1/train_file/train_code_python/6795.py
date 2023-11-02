def solution():
    """There are 35 bottles of milk on the grocery store shelf. Jason buys 5 of the bottles and Harry buys 6 more. How many bottles of milk are left on the store shelf after Jason and Harry purchased milk?"""
    initial_bottles = 35
    bottles_bought_jason = 5
    bottles_bought_harry = 6
    bottles_left = initial_bottles - bottles_bought_jason - bottles_bought_harry
    result = bottles_left
    return result

print(solution())