def solution():
    uphill_speed = 2
    downhill_speed = 3
    uphill_distance = 5 * 0.6
    downhill_distance = 5 * 0.4
    uphill_time = uphill_distance / uphill_speed
    downhill_time = downhill_distance / downhill_speed
    total_time = uphill_time + downhill_time
    result = total_time
    return result

Question: If Sally can paint a house in 5 hours and motherboard in 3 hours, how long will it take her to do both if she works on the house for 2 hours, then she work on the motherboard for 1 hour, then she works on the house for another hour?
Solution:
def solution():
    painting_time = 5
    motherboard_time = 3
    painting_time_left = painting_time - 2
    motherboard_time_left = motherboard_time - 1
    time_left = painting_time_left + motherboard_time_left
    result = time_left
    return result

print(solution())