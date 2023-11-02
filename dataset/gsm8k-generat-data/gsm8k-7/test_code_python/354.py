def solution():
    boxes_left = 4

    # Set up equation based on the information given
    # Let x be the number of boxes Seth bought in the first place
    # x - 1 (box given to mother) - (x - 1)/2 (half given away) = 4
    # Solving for x:
    x = (boxes_left + 1) * 2

    result = x
    return result

print(solution())