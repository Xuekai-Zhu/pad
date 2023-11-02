def solution():
    """Chris buys 2 and a half dozen donuts on his way to work to share with his co-workers. While driving, he eats 10% of the donuts. Once inside, he grabs another 4 donuts for his afternoon snack. How many donuts are left for his co-workers?"""
    donuts_bought = 2.5 * 12
    donuts_eaten = int(donuts_bought * 0.1)
    remaining_donuts = donuts_bought - donuts_eaten - 4
    result = remaining_donuts
    return result

print(solution())