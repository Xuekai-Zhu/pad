def solution():
    num_dress_shirts = 4
    dress_shirt_price = 15.0

    num_pants = 2
    pants_price = 40.0

    num_sweaters = 2
    sweater_price = 30.0

    suit_price = 150.0

    discount1 = 0.20  # 20% discount from store
    discount2 = 0.10  # 10% off coupon

    # Calculate the total cost of all items without any discounts
    total_cost = (num_dress_shirts * dress_shirt_price) + (num_pants * pants_price) + \
                 (num_sweaters * sweater_price) + suit_price

    # Calculate the total discount from the store's 20% discount
    store_discount = total_cost * discount1

    # Calculate the total cost after the store's discount
    total_cost -= store_discount

    # Calculate the total cost after the additional 10% off coupon
    total_cost *= (1 - discount2)

    result = total_cost
    return result

print(solution())