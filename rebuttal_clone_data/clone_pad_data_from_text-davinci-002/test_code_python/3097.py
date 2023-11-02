def solution():
     Theon_speed = 15
     Yara_speed = 30
     distance = 90
     hours_needed = distance / Yara_speed
     Theon_hours_needed = distance / Theon_speed
     difference = hours_needed - Theon_hours_needed
     result = difference
     return result

print(solution())