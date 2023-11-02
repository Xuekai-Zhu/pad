def solution():
    toaster_cost = 30  # MSRP of toaster
    insurance_cost = toaster_cost * 0.2  # insurance plan cost
    total_cost = (toaster_cost + insurance_cost) * 1.5  # add state tax of 50% after insurance plan cost calculation
    result = total_cost
    return result

print(solution())