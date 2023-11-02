def solution():
    total_guests = 80
    steak_guests = total_guests / 3
    chicken_guests = total_guests - steak_guests
    steak_cost = 25
    chicken_cost = 18
    catering_budget = (steak_guests * steak_cost) + (chicken_guests * chicken_cost)
    result = catering_budget
    return result

print(solution())