def solution():
    machines_total = 3 + 1  # There will be 4 machines in total
    hours_total = 23 + 12  # The machines will work for 23 + 12 = 35 hours in a day
    production_per_hour = machines_total * 2  # Each machine produces 2 kg of material every hour
    total_production = production_per_hour * hours_total  # Total amount of material produced in a day
    total_earnings = total_production * 50  # Total earnings from selling the material at $50 per kg
    result = total_earnings
    return result

print(solution())