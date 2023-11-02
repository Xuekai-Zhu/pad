def solution():
     shots_attempted = 20
     percentage = 80
     shots_made = shots_attempted * (percentage / 100)
     shots_missed = shots_attempted - shots_made
     result = shots_missed
     return result

print(solution())