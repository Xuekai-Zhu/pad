def solution():
    monica_money = 15
    michelle_money = 12
    cake_cost = 15
    soda_cost = 3
    num_guests = 8

    # Calculate total money available for soda
    total_money = monica_money + michelle_money - cake_cost
    num_soda_bottles = total_money // soda_cost

    # Calculate total servings of soda
    total_soda_servings = num_soda_bottles * 12

    # Calculate servings per guest
    servings_per_guest = total_soda_servings / num_guests
    result = servings_per_guest
    return result

print(solution())