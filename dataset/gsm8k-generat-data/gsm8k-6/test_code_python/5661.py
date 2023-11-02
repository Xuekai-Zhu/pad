def solution():
    # Calculate the total amount raised by the fundraiser
    stack_price = 4.00 # cost of a stack of pancakes
    bacon_price = 2.00 # cost of adding bacon to a stack of pancakes
    total_stacks = 60 # number of stacks of pancakes sold
    total_bacon = 90 # number of slices of bacon sold
    total_raised = (stack_price * total_stacks) + (bacon_price * total_bacon)
    result = total_raised
    return result

print(solution())