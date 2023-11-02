def solution():
    feet_traveled = 5 * 11 - 2 * 11
    result = feet_traveled
    return result
 
Question: A tank is being filled with water. Every minute, the water level rises three inches. How many hours will it take to fill an empty tank that is 18 feet tall?
Solution:
def solution():
    inches_to_feet = 1/12
    minutes_to_hours = 1/60
    rise_per_minute = 3 * inches_to_feet
    tank_height = 18
    time_to_fill = tank_height / rise_per_minute * minutes_to_hours
    result = time_to_fill
    return result

print(solution())