def solution():
     visitors_per_hour = 50
     hours_per_day = 24
     days_per_month = 30
     revenue_per_visitor = 0.10
     total_revenue = visitors_per_hour * hours_per_day * days_per_month * revenue_per_visitor
     result = total_revenue
     return result

print(solution())