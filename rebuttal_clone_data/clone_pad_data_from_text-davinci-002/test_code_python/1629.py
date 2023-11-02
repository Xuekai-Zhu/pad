def solution():
    visitors_per_hour = 50
    hours_open = 8
    total_visitors = visitors_per_hour * hours_open
    Gorilla_visitors_percent = 80
    Gorilla_visitors = total_visitors * (Gorilla_visitors_percent/100)
    result = Gorilla_visitors
    return result

print(solution())