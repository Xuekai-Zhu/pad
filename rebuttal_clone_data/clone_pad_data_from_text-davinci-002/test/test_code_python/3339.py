def solution():
     kickers_first = 2
     kickers_second = kickers_first * 2
     spiders_first = kickers_first / 2
     spiders_second = kickers_second * 2
     total_goals = kickers_first + kickers_second + spiders_first + spiders_second
     result = total_goals
     return result

print(solution())