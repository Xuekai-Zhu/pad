def solution():
    # Calculate the number of bottle caps Marla needs to buy a horse
    horse_value = 80 * 3 / 5 * 8 # 3 lizards are worth 5 gallons of water and 1 lizard is worth 8 bottle caps
    horse_cost = horse_value / 8 # 1 lizard is worth 8 bottle caps
    total_caps_needed = horse_cost * 20 + 4 # Marla needs to collect this many bottle caps to buy a horse

    # Calculate the number of days it will take Marla to collect enough bottle caps
    days_needed = total_caps_needed / 20
    result = days_needed
    return result

print(solution())