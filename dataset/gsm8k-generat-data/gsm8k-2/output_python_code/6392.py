def solution():
    """Alex has not washed his clothes for a month; 18 shirts, 12 pants, 17 sweaters, and 13 jeans are waiting to be washed. Alex's washing machine can wash a maximum of 15 items per cycle. Each cycle takes 45 minutes. How many hours will it take the washing machine to wash all the clothes?"""
    total_clothes = 18 + 12 + 17 + 13
    cycles_needed = total_clothes // 15
    if total_clothes % 15 != 0:
        cycles_needed += 1
    washing_time = cycles_needed * 45
    washing_time_in_hours = washing_time / 60
    result = washing_time_in_hours
    return result

print(solution())