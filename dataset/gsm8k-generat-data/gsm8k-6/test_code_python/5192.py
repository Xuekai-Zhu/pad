def solution():
    # Calculate the total amount spent
    total_spent = (3*11) + (8*4) + (3*6) + 37  # cost of beef, fruits/vegetables, spices, and other groceries

    # Calculate the prize points
    points_per_10 = 50
    bonus_points = 250 if total_spent > 100 else 0
    prize_points = int((total_spent/10) * points_per_10) + bonus_points

    result = prize_points
    return result

print(solution())