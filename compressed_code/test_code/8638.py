def solution():
    
    first_week_donation = 40
    second_week_donation = first_week_donation * 2
    total_donation = first_week_donation + second_week_donation
    donated_food = total_donation * 0.7
    remaining_food = total_donation - donated_food
    result = remaining_food
    return result

print(solution())