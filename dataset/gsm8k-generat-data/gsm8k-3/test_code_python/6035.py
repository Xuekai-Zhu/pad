def solution():
    """Cherry put up a delivery service. She charges $2.50 for a 3-5 kilograms cargo and $4 for a 6-8 kilograms cargo. If she delivers four 5 kilograms cargo and two 8 kilograms cargo per day, how much money will she earn in a week?"""
    # Define the cargo weight ranges and their corresponding prices
    PRICE_RANGE_1 = {'min': 3, 'max': 5, 'price': 2.5}
    PRICE_RANGE_2 = {'min': 6, 'max': 8, 'price': 4}

    # Define the cargo weights and quantities for each day
    day_1 = [{'weight': 5, 'quantity': 4}, {'weight': 8, 'quantity': 2}]
    day_2 = [{'weight': 5, 'quantity': 4}, {'weight': 8, 'quantity': 2}]
    day_3 = [{'weight': 5, 'quantity': 4}, {'weight': 8, 'quantity': 2}]
    day_4 = [{'weight': 5, 'quantity': 4}, {'weight': 8, 'quantity': 2}]
    day_5 = [{'weight': 5, 'quantity': 4}, {'weight': 8, 'quantity': 2}]
    day_6 = [{'weight': 5, 'quantity': 4}, {'weight': 8, 'quantity': 2}]
    day_7 = [{'weight': 5, 'quantity': 4}, {'weight': 8, 'quantity': 2}]

    # Calculate the total earnings for the week
    total_earnings = 0
    for day in [day_1, day_2, day_3, day_4, day_5, day_6, day_7]:
        for cargo in day:
            weight = cargo['weight']
            quantity = cargo['quantity']
            if weight >= PRICE_RANGE_1['min'] and weight <= PRICE_RANGE_1['max']:
                price = PRICE_RANGE_1['price']
            elif weight >= PRICE_RANGE_2['min'] and weight <= PRICE_RANGE_2['max']:
                price = PRICE_RANGE_2['price']
            else:
                price = 0
            total_earnings += price * quantity

    # Display the total earnings for the week
    result = total_earnings
    return result

print(solution())