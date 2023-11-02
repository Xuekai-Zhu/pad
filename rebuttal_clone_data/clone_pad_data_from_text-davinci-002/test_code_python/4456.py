def solution():
     sheets_per_day = 200
     total_sheets = 9000
     days_in_week = 5
     sheets_per_class = sheets_per_day * days_in_week
     total_classes = total_sheets / sheets_per_class
     result = total_classes
     return result

print(solution())