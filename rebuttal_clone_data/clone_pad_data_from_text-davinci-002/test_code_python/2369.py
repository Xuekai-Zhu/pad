def solution(): 
     daily_rate = 50
     two_week_rate = 500
     days_requested = 20
     cost = two_week_rate * (days_requested // 14) + daily_rate * (days_requested % 14)
     result = cost
     return result

print(solution())