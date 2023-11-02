def solution():
    num_basketballs = 10
    basketball_price = 29

    num_baseballs = 14
    baseball_price = 2.5

    baseball_bat_price = 18

    # Calculate the total cost of the basketballs
    total_basketballs_cost = num_basketballs * basketball_price

    # Calculate the total cost of the baseballs
    total_baseballs_cost = num_baseballs * baseball_price

    # Calculate the total cost of the baseball bat
    total_bat_cost = baseball_bat_price

    # Calculate the total amount spent by coach A
    coach_a_total = total_basketballs_cost

    # Calculate the total amount spent by coach B
    coach_b_total = total_baseballs_cost + total_bat_cost

    # Calculate the difference in the amount spent by both coaches
    difference = coach_a_total - coach_b_total
    result = difference
    return result

print(solution())