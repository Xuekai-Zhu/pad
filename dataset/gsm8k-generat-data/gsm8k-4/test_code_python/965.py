def solution():
    """Sarah, Mary, and Tuan decided to go to the restaurant for a meal. They decided to split the cost of the meal evenly. If the total price of the meal comes to $67 and they have a coupon for $4, how much does each person need to contribute to the bill?"""
    # Define the total price of the meal and the coupon value
    total_price = 67
    coupon = 4

    # Subtract the value of the coupon from the total price
    net_price = total_price - coupon

    # Divide the net price equally between the three friends
    per_person_price = net_price / 3

    # Round the result to two decimal places
    result = round(per_person_price, 2)
    return result

print(solution())