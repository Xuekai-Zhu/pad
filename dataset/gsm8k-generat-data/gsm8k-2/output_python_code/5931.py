def solution():
    """Jenine can sharpen a pencil 5 times before it runs out. She needs to sharpen a pencil for every 1.5 hours of use. She already has ten pencils and needs to write for 105 hours. A new pencil costs $2. How much does she need to spend on more pencils to be able to write for 105 hours?"""
    pencils_per_hour = 1.5 / 5
    total_pencils_needed = 105 / pencils_per_hour
    current_pencils = 10
    pencils_to_buy = total_pencils_needed - current_pencils
    cost_per_pencil = 2
    total_cost = pencils_to_buy * cost_per_pencil
    result = total_cost
    return result

print(solution())