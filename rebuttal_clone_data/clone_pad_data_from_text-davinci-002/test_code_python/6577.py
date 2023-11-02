def solution():
     passing_score = 50
     points_earned = 60
     points_lost = 15
     points_needed = passing_score - points_earned
     points_allowed_to_lose = points_needed + points_lost
     result = points_allowed_to_lose
     return result

print(solution())