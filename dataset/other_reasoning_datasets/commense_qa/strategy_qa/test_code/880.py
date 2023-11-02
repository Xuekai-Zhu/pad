def solution():
    preventive_healthcare_covered = True
    sick_visits_billed_separately = True
    if preventive_healthcare_covered and sick_visits_billed_separately:
        result = "yes, you need to schedule separate visits"
    else:
        result = "no, you may be able to schedule both types of visits in one appointment"
    return result

print(solution())