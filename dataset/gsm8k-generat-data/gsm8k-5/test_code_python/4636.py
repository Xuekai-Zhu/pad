def solution():
    initial_biscuits = 32  # Randy had 32 biscuits
    gift_biscuits = 13  # His father gave him 13 biscuits
    mother_biscuits = 15  # His mother gave him 15 biscuits
    eaten_biscuits = 20  # His brother ate 20 of these biscuits

    # Calculate the total number of biscuits Randy is left with
    total_biscuits = initial_biscuits + gift_biscuits + mother_biscuits - eaten_biscuits
    result = total_biscuits
    return result

print(solution())