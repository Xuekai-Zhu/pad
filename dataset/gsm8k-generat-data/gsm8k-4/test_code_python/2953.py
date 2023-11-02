def solution():
    """There is a pie-eating contest at school. Adam eats three more pies than Bill. Sierra eats twice as many pies as Bill. If Sierra ate 12 pies, how many pies were eaten in total?"""
    # Calculate the number of pies Bill ate
    bill_pies = 12/2

    # Calculate the number of pies Adam ate
    adam_pies = bill_pies + 3

    # Calculate the total number of pies eaten
    total_pies = bill_pies + adam_pies + 12

    result = total_pies
    return result

print(solution())