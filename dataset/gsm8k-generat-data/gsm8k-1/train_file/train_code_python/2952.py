def solution():
    """There is a pie-eating contest at school. Adam eats three more pies than Bill. Sierra eats twice as many pies as Bill. If Sierra ate 12 pies, how many pies were eaten in total?"""
    sierra_pies = 12
    bill_pies = sierra_pies / 2
    adam_pies = bill_pies + 3
    total_pies = sierra_pies + bill_pies + adam_pies
    result = total_pies
    return result

print(solution())