def solution():
    # Calculate the total amount of food needed for 4 dogs for 14 days
    total_food = 4 * 250 * 14 / 1000  # 4 dogs each eat 250 grams of food per day, for 14 days. Convert to kilograms
    result = total_food
    return result

print(solution())