def solution():
    """Alex has not washed his clothes for a month; 18 shirts, 12 pants, 17 sweaters, and 13 jeans are waiting to be washed. Alex's washing machine can wash a maximum of 15 items per cycle. Each cycle takes 45 minutes. How many hours will it take the washing machine to wash all the clothes?"""
    # Calculate the total number of clothes that need to be washed
    total_clothes = 18 + 12 + 17 + 13

    # Calculate the number of cycles needed to wash all the clothes
    num_cycles = total_clothes // 15
    if total_clothes % 15 != 0:
        num_cycles += 1

    # Calculate the time needed to wash all the clothes
    time_minutes = num_cycles * 45
    time_hours = time_minutes / 60

    # Return the result
    result = time_hours
    return result

print(solution())