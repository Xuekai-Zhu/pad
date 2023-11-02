def solution():
    """John collects garbage from 3 different apartment complexes. The first two have 200 apartments each and the last one is 60% bigger than the other two combined. He collects garbage 3 times a week from each place and he gets paid $.40 per collection for each apartment. How much money does he make in a week?"""
    apartments_1 = 200
    apartments_2 = 200
    apartments_3 = (apartments_1 + apartments_2) * 1.6
    collections_per_week = 3 * (apartments_1 + apartments_2 + apartments_3)
    pay_per_collection = .4
    total_pay = collections_per_week * pay_per_collection
    result = total_pay
    return result

print(solution())