def solution():
    total_slices = 8 * 2 # 8 pieces, each cut into 2 slices
    friend_slices = 2 # friend eats 2 slices
    remaining_slices = total_slices - friend_slices # subtract friend's slices from total
    james_slices = remaining_slices // 2 # James eats half of remaining slices
    result = james_slices
    return result

print(solution())