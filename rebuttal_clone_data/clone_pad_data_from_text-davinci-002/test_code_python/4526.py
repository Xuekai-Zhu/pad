def solution():
    vaccines = 10
    vaccines_paid = 45 * 10
    doctor_visit = 250
    trip_cost = 1200
    percent_covered = 80
    vaccines_percent_covered = vaccines_paid * (percent_covered / 100)
    doctor_visit_percent_covered = doctor_visit * (percent_covered / 100)
    amount_owed = vaccines_paid + doctor_visit - (vaccines_percent_covered + doctor_visit_percent_covered) + trip_cost
    result = amount_owed
    
    return result

print(solution())