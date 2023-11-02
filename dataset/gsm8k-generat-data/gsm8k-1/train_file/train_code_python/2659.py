def solution():
    """Mr. Salazar had seven dozen oranges. He reserved 1/4 of it for his friend and was able to sell 3/7 of the remaining yesterday. Today, he saw four rotten oranges. How many oranges are left to be sold today?"""
    total_oranges = 7 * 12
    oranges_reserved = total_oranges * (1/4)
    oranges_remaining = total_oranges - oranges_reserved
    oranges_sold_yesterday = oranges_remaining * (3/7)
    oranges_left = oranges_remaining - oranges_sold_yesterday - 4
    result = oranges_left
    return result

print(solution())