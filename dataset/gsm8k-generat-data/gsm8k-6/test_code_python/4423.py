def solution():
    # Calculate the total amount of money they have to spend
    total_money = 15 + 12  # Monica brings $15 and Michelle brings $12

    # Calculate the number of soda bottles they can buy
    soda_cost = 3  # cost per bottle of soda
    max_soda_bottles = (total_money - 15) // soda_cost  # they can spend $15 on the cake, rest is for soda
    total_soda_servings = max_soda_bottles * 12  # each bottle of soda has 12 servings

    # Calculate the number of soda servings each guest gets
    num_guests = 8
    servings_per_guest = total_soda_servings // num_guests

    result = servings_per_guest
    return result

print(solution())