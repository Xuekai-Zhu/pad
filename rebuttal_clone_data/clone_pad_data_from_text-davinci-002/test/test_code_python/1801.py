def solution():
    hour_rate_old = 16
    hour_rate_new = 12
    Scream_charge = 3
    babysitting_hours = 6
    frequency_of_screaming = 2
    hour_rate_old_total = hour_rate_old * babysitting_hours
    hour_rate_new_total = (hour_rate_new * babysitting_hours) + (Scream_charge * frequency_of_screaming)
    total_cost_difference = hour_rate_old_total - hour_rate_new_total
    result = total_cost_difference
    return result

print(solution())