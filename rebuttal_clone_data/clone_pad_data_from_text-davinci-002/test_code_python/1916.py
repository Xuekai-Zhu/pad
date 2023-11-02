def solution():
    donaldson_rate = 15
    donaldson_hours = 7
    merck_rate = 18
    merck_hours = 6
    hille_rate = 20
    hille_hours = 3
    
    total_hours = donaldson_hours + merck_hours + hille_hours
    total_earnings = (donaldson_rate * donaldson_hours) + (merck_rate * merck_hours) + (hille_rate * hille_hours)
    
    result = total_earnings
    
    return result

print(solution())