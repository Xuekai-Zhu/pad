def solution():
    num_horses = 4  # Peter has four horses
    oats_per_day = 4 * 2  # Each horse eats 4 pounds of oats twice per day
    grain_per_day = 3  # Each horse eats 3 pounds of grain once per day
    days = 3  # Peter needs to feed his horses for 3 days

    # Calculate the total amount of oats and grain Peter needs to feed his horses
    total_oats = num_horses * oats_per_day * days
    total_grain = num_horses * grain_per_day * days

    # Calculate the total amount of food Peter needs to feed his horses
    total_food = total_oats + total_grain
    result = total_food
    return result

print(solution())