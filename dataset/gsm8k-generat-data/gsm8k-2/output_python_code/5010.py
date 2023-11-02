def solution():
    """The local salon offers mani/pedis for $40.00. They are running a Mother's day special and offering 25% off their regular rate. Charlotte is treating herself, her daughter and 3 granddaughters to a spa day. How much will Charlotte spend on 5 mani/pedis?"""
    original_price = 40
    discount = 0.25
    discounted_price = original_price * (1 - discount)
    num_people = 5
    total_cost = num_people * discounted_price
    result = total_cost
    return result

print(solution())