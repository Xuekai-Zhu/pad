def solution():
    # Calculate the number of bottle caps Marla needs to buy a horse
    horse_cost = 80 * (5/3) * 8  # 3 lizards are worth 5 gallons of water, and 1 lizard is worth 8 bottle caps
    bottle_cap_cost = horse_cost  # the cost of a horse in bottle caps is the same as in water
    food_shelter_cost = 4 * 30  # Marla needs to pay 4 bottle caps per night for food and shelter for 30 days
    total_cost = bottle_cap_cost + food_shelter_cost  # total bottle cap cost
    days_to_collect = total_cost / 20  # Marla can scavenge for 20 bottle caps each day
    result = days_to_collect
    return result

print(solution())