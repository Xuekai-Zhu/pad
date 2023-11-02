def solution():
    filming_budget = 500000
    box_office_earnings = 60000000
    if box_office_earnings > filming_budget:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())