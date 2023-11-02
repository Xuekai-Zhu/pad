def solution():
    commencement_months = ["December", "May", "June"]
    frost_months = ["December"]
    overlap = [month for month in commencement_months if month in frost_months]
    if overlap:
        result = "yes, it is common to see frost during some college commencements."
    else:
        result = "no, it is not common to see frost during college commencements."
    return result

print(solution())