def solution():
    """Emani has $30 more money than Howard. If Emani has $150, and they decide to combine and share the money equally, how much money does each get?"""
    # Define Emani's and Howard's money
    emani_money = 150
    howard_money = emani_money - 30

    # Calculate the total money they have
    total_money = emani_money + howard_money

    # Divide the total money equally
    each_get = total_money / 2

    # Return the result
    result = each_get
    return result

print(solution())