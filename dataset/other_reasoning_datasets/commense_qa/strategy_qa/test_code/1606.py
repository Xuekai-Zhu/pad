def solution():
    autumn_months = ["September", "October", "November", "December"]
    hibernation_months = ["September", "October", "November", "December", "January", "February", "March", "April"]
    overlap = [month for month in autumn_months if month in hibernation_months]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())