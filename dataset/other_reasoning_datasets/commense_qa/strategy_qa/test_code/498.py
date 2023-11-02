def solution():
    # Define the months of the US presidential election and bee hibernation
    election_month = "November"
    bee_hibernation_months = ["December", "January", "February"]

    # Check if there is an overlap between the two months
    overlap = [month for month in bee_hibernation_months if month == election_month]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())