def solution():
    number_of_epipens = 2
   cost_of_epipen = 500
    percent_covered = 75
    amount_paid = (number_of_epipens * cost_of_epipen) * (1 - (percent_covered / 100))
    result = amount_paid
    return result

print(solution())