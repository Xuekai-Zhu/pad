def solution():
    """Sarah, Mary, and Tuan decided to go to the restaurant for a meal. They decided to split the cost of the meal evenly. If the total price of the meal comes to $67 and they have a coupon for $4, how much does each person need to contribute to the bill?"""
    total_price = 67
    discount = 4
    final_price = total_price - discount

    num_people = 3
    per_person_price = final_price / num_people

    result = per_person_price
    return result

print(solution())