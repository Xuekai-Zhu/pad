def solution():
    """Emani has $30 more money than Howard. If Emani has $150, and they decide to combine and share the money equally, how much money does each get?"""
    # Determine how much money Howard has
    howard_money = 150 - 30

    # Determine the total money they have combined
    total_money = howard_money + 150

    # Divide the total money by 2 to determine how much each gets
    each_gets = total_money / 2

    # Display how much each gets
    result = each_gets
    return result

print(solution())