def solution():

    lawn_mowing_rate = 6
    weed_removal_rate = 11
    mulch_laying_rate = 9

    hours_spent_mowing_lawn = 63
    hours_spent_removing_weeds = 9
    hours_spent_laying_mulch = 10

    total_revenue = (lawn_mowing_rate * hours_spent_mowing_lawn) + (weed_removal_rate * hours_spent_removing_weeds) + (mulch_laying_rate * hours_spent_laying_mulch)
    
    return total_revenue

print(solution())