def solution():
    """Jerry had 63 pieces of candy. He divided them up equally into 9 bags. 2 of the bags had chocolate hearts. 3 of the bags were chocolate kisses. The rest of the bags were not chocolate. How many pieces of candy were not chocolate?"""
    total_candy = 63
    bags = 9
    chocolate_bags = 2 + 3
    non_chocolate_bags = bags - chocolate_bags
    non_chocolate_candy = (total_candy // bags) * non_chocolate_bags
    result = non_chocolate_candy
    return result

print(solution())