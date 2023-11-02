def solution():
    """A hotel in the Philippines charges 1000 pesos for a 12-hour stay or 1600 pesos for a 24-hour stay. After 12 hours, visitors have the option to add 70 pesos for every additional hour. Cameron arrives at 5 pm at the hotel and wants to leave at 10 am the next morning. He decides to go with the option of adding on 70 pesos for every hour after the 12-hour mark instead of paying for 24 hours. How much money would Cameron save?"""
    cost_12_hours = 1000
    cost_24_hours = 1600
    additional_cost = 70
    hours_in_hotel = (10 + 12 - 5)  # 10 am check-out time, and he arrives at 5 pm the previous day
    if hours_in_hotel <= 12:
        total_cost = cost_12_hours
    else:
        total_cost = cost_12_hours + (hours_in_hotel - 12) * additional_cost
    saved_cost = cost_24_hours - total_cost
    result = saved_cost
    return result

print(solution())