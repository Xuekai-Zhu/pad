def solution():
    dogs_per_walk = 3  # Johnny can walk 3 dogs at once
    pay_30min = 15  # Johnny is paid $15 for a 30-minute walk
    pay_60min = 20  # Johnny is paid $20 for a 60-minute walk
    hours_per_day = 4  # Johnny works for 4 hours per day
    days_per_week = 5  # Johnny works for 5 days per week
    total_dogs = 6 + (dogs_per_walk * (4 * hours_per_day * days_per_week - 6))  # Johnny always walks the maximum number of dogs

    # Calculate the total pay for the 30-minute walks
    pay_30_total = (total_dogs // dogs_per_walk) * pay_30min

    # Calculate the total pay for the 60-minute walks
    pay_60_total = 6 * pay_60min  # Johnny walks 6 dogs for 60 minutes each day

    # Calculate the total money Johnny makes in a week
    total_money = pay_30_total + pay_60_total
    result = total_money
    return result

print(solution())