def solution():
    # Calculate the total time Anna spends sweeping
    anna_time = 3 * 10  # 3 minutes per room, and Anna is sweeping 10 rooms
    # Calculate the total time Billy spends doing laundry
    billy_time = 9 * 2  # 9 minutes per load, and Billy is doing 2 loads of laundry
    # Calculate the total time Billy needs to spend washing dishes to match Anna's time
    total_time = (anna_time + billy_time) / 2  # Calculate the average time spent by Anna and Billy
    dishes_time = total_time - billy_time  # Subtract the time spent by Billy on laundry from the average time
    # Calculate the number of dishes Billy needs to wash in the remaining time
    dishes_to_wash = dishes_time / 2  # Each dish takes 2 minutes to wash
    result = dishes_to_wash
    return result

print(solution())