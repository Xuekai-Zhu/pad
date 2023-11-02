def solution():
    pasture_rent = 500 * 12  # Andrea pays $500/month to rent a pasture for the pony, so $6,000 a year
    food_cost = 10 * 365  # Andrea pays $10 a day for food which amounts to $3650 a year
    lesson_cost = 60 * 2 * 52  # Andrea takes two lessons a week, which amounts to 104 lessons a year, each costing $60, so $6,240 a year
    total_cost = pasture_rent + food_cost + lesson_cost  # Total cost of keeping the pony for a year
    result = total_cost
    return result

print(solution())