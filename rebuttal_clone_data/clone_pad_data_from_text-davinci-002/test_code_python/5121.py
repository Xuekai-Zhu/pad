def solution():
     rhinestones_needed = 45
     rhinestones_bought = 45 / 3
     rhinestones_found = 45 / 5
     rhinestones_remaining = rhinestones_needed - rhinestones_bought - rhinestones_found
     result = rhinestones_remaining
     return result

print(solution())