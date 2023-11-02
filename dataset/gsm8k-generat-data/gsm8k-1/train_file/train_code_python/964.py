def solution():
    """Sarah, Mary, and Tuan decided to go to the restaurant for a meal. They decided to split the cost of the meal evenly. If the total price of the meal comes to $67 and they have a coupon for $4, how much does each person need to contribute to the bill?"""
    total_price = 67
    coupon = 4
    price_after_coupon = total_price - coupon
    num_people = 3
    each_person_price = price_after_coupon / num_people
    result = each_person_price
    return result

print(solution())