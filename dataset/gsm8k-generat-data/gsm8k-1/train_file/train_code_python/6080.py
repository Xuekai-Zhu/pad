def solution():
    """Joe sells cookies for 20% more than it costs to make them. If he sold 50 cookies and earned $60, how much do the cookies cost to make?"""
    selling_price = 60 / 50  # price per cookie
    cost_price = selling_price / 1.2  # cost per cookie
    result = cost_price
    return result

print(solution())