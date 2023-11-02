def solution():
    initial_saving = 2
    total_saving = initial_saving  # initialize total savings with the initial saving amount
    for i in range(2, 7):
        month_saving = 2**(i-1)  # saving amount for the ith month
        total_saving += month_saving  # add the month's saving to the total saving
    result = total_saving
    return result

print(solution())