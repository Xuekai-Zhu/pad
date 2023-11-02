def solution():
     paintings_painted = 12
     hours_taken = 6
     paintings_remaining = 20
     hours_remaining = (paintings_remaining / paintings_painted) * hours_taken
     total_hours = hours_taken + hours_remaining
     result = total_hours
     return result

print(solution())