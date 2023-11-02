def solution():
     total_days = 3
     travel_days = 2
     days_at_grandparents = 5
     days_at_brothers = 5
     days_at_sisters = total_days - (travel_days + days_at_grandparents + days_at_brothers)
     result = days_at_sisters
     return result

print(solution())