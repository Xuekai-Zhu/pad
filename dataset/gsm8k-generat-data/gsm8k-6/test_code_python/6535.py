def solution():
    # Calculate the total number of bracelets Trey needs to sell
    total_bracelets = 112  # the cost of the bike is $112 and he sells each bracelet for $1
    days = 14  # he plans to sell bracelets for the next two weeks
    bracelets_per_day = total_bracelets / days  # average bracelets sold per day
    result = bracelets_per_day
    return result

print(solution())