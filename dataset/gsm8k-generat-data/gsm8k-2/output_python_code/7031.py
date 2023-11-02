def solution():
    """Chris buys 2 and a half dozen donuts on his way to work to share with his co-workers. While driving, he eats 10% of the donuts. Once inside, he grabs another 4 donuts for his afternoon snack. How many donuts are left for his co-workers?"""
    donuts_bought = 2.5 * 12
    donuts_left_after_driving = donuts_bought * 0.9
    donuts_left_after_afternoon_snack = donuts_left_after_driving - 4
    result = donuts_left_after_afternoon_snack
    return result

print(solution())