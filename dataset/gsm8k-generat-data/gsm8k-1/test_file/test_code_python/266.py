def solution():
    """Mary buys 3 bags of M&Ms. The first bag has 300 M&Ms in it. The second bag has 12 more M&Ms than the first, and the third bag has a hole in it, so it only has half the number of M&Ms that the first bag had. How many M&Ms did Mary get total?"""
    first_bag = 300
    second_bag = first_bag + 12
    third_bag = first_bag / 2
    total_mms = first_bag + second_bag + third_bag
    result = total_mms
    return result

print(solution())