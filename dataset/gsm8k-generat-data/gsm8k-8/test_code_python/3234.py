def solution():
    # Calculate half of the total amount
    half_amount = 124600 / 2

    # Calculate the amount to be divided among the remaining grandchildren
    remaining_amount = 124600 - half_amount

    # Calculate the amount each grandchild will receive
    each_grandchild = remaining_amount / 10
    result = each_grandchild
    return result

print(solution())