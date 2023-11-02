def solution():
    """The local salon offers mani/pedis for $40.00. They are running a Mother's day special and offering 25% off their regular rate. Charlotte is treating herself, her daughter and 3 granddaughters to a spa day. How much will Charlotte spend on 5 mani/pedis?"""
    regular_rate = 40.00
    discount_percent = 25
    discounted_rate = regular_rate - (regular_rate * (discount_percent / 100))
    num_people = 5
    total_cost = discounted_rate * num_people
    result = total_cost
    return result

print(solution())