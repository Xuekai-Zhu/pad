def solution():
    total_trees = 4000
    spruce_percent = 10
    pine_percent = 13
    oak_percent = (spruce_percent + pine_percent)
    birch_percent = 100 - (spruce_percent + pine_percent + oak_percent)
    spruce_amount = total_trees * (spruce_percent / 100)
    pine_amount = total_trees * (pine_percent / 100)
    oak_amount = total_trees * (oak_percent / 100)
    birch_amount = total_trees * (birch_percent / 100)
    result = birch_amount
    return result

print(solution())