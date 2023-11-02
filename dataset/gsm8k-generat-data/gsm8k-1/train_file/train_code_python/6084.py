def solution():
    """Carol spends five hours filling up her pool. During the first hour, the pool fills at a rate of 8 gallons of water per hour. For the next two hours, the pool fills at 10 gallons of water per hour. For the fourth hour, the pool fills at a rate of 14 gallons of water per hour. During the fifth hour, the pool develops a leak and loses 8 gallons of water. At the end of five hours, how many gallons of water are still left in the pool?"""
    initial_fill = 8
    second_hour_fill = 10
    third_hour_fill = 10
    fourth_hour_fill = 14
    leak = 8
    total_fill = initial_fill + (second_hour_fill * 2) + fourth_hour_fill - leak
    result = total_fill
    return result

print(solution())