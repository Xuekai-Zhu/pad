def solution():
    """Jenine can sharpen a pencil 5 times before it runs out. She needs to sharpen a pencil for every 1.5 hours of use. She already has ten pencils and needs to write for 105 hours. A new pencil costs $2. How much does she need to spend on more pencils to be able to write for 105 hours?"""
    pencils = 10
    sharpenings_per_pencil = 5
    sharpenings_per_hour = 1.5
    total_hours_needed = 105
    hours_per_pencil = sharpenings_per_pencil * sharpenings_per_hour
    pencils_needed = (total_hours_needed // hours_per_pencil) + 1 - pencils
    cost_per_pencil = 2
    total_cost = pencils_needed * cost_per_pencil
    result = total_cost
    return result

print(solution())