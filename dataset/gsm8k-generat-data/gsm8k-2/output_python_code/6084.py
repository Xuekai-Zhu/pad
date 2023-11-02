def solution():
    """Carol spends five hours filling up her pool. During the first hour, the pool fills at a rate of 8 gallons of water per hour. For the next two hours, the pool fills at 10 gallons of water per hour. For the fourth hour, the pool fills at a rate of 14 gallons of water per hour. During the fifth hour, the pool develops a leak and loses 8 gallons of water. At the end of five hours, how many gallons of water are still left in the pool?"""
    total_time = 5
    first_hour = 8
    second_two_hours = 10 * 2
    fourth_hour = 14
    leak = 8

    total_filled = first_hour + second_two_hours + fourth_hour
    total_filled -= leak
    remaining_time = total_time - 4
    remaining_fill = remaining_time * total_filled
    total_fill = first_hour + second_two_hours + fourth_hour + remaining_fill
    leaked_gallons = leak * 1
    remaining_gallons = total_fill - leaked_gallons
    result = remaining_gallons
    return result

print(solution())