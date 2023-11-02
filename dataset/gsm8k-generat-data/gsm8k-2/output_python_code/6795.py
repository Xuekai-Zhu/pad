def solution():
    """There are 35 bottles of milk on the grocery store shelf. Jason buys 5 of the bottles and Harry buys 6 more. How many bottles of milk are left on the store shelf after Jason and Harry purchased milk?"""
    initial_bottles = 35
    jason_buys = 5
    harry_buys = 6
    remaining_bottles = initial_bottles - jason_buys - harry_buys
    result = remaining_bottles
    return result

print(solution())