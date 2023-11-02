def solution():
    
    first_week_donation = 40
    second_week_donation = 2 * first_week_donation
    total_donation = first_week_donation + second_week_donation
    donated_to_homeless = 0.7 * total_donation
    remaining_food = total_donation - donated_to_homeless
    result = remaining_food
    return result

print(solution())