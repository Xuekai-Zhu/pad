def solution():
     ounces_per_tablet = 4
     pills_per_day = 3
     days_forgotten = 2
     days_taken = 7
     total_ounces = (ounces_per_tablet * pills_per_day * days_taken) - (ounces_per_tablet * days_forgotten)
     result = total_ounces
    return result

print(solution())