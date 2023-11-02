def solution():
    forms_per_hour = 25
    hours_per_day = 8
    forms_per_day = 2400

    # Calculate the total number of forms that can be processed in one day by one clerk
    forms_per_clerk = forms_per_hour * hours_per_day

    # Calculate the number of clerks needed to process all the forms in one day
    num_clerks = forms_per_day // forms_per_clerk + 1  # add 1 to account for partial hours

    result = num_clerks
    return result

print(solution())