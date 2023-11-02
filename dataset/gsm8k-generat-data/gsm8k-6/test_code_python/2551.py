def solution():
    # Calculate the total points Duke scored in the final game
    points_scored = 5*1 + 4*2 + 17  # 5 free throws worth one point each, 4 regular baskets worth two points each, and 17 more points to tie the record

    # Calculate how many three-pointers Duke normally scores in a game
    normal_three_pointers = 2

    # Calculate how many three-pointers Duke scored in the final game
    final_three_pointers = (points_scored - 257 - normal_three_pointers*2) / 3

    result = final_three_pointers - normal_three_pointers
    return result

print(solution())