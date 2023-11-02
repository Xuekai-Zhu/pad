def solution():
    sierra_pies = 12  # Sierra ate 12 pies
    bill_pies = sierra_pies / 2  # Bill ate half as many pies as Sierra
    adam_pies = bill_pies + 3  # Adam ate three more pies than Bill

    # Calculate the total number of pies eaten
    total_pies = sierra_pies + bill_pies + adam_pies
    result = total_pies
    return result

print(solution())