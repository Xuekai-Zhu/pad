def solution():
    # Calculate the total cost of blue pens
    blue_cost = 10 * 0.1  # 10 blue pens cost 10 cents each

    # Calculate the total cost of red pens
    red_cost = 15 * 0.2  # 15 red pens cost twice as much as a blue pen, which is 20 cents

    # Calculate the total cost of all pens
    total_cost = blue_cost + red_cost
    result = total_cost
    return result

print(solution())