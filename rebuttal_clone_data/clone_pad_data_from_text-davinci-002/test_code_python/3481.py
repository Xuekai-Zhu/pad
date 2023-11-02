def solution():
     marbles_now = 30
     marbles_given_away = 60 + (2*60) + (3*30)
     marbles_started_with = marbles_now + marbles_given_away
     result = marbles_started_with
     return result

print(solution())