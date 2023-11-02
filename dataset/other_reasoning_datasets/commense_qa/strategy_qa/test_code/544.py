def solution():
    darth_vader_height = 6.2
    bill_walton_height = 6.11
    rim_height = 10
    darth_vader_reach = darth_vader_height + 1 # assuming an extra foot for arm span
    bill_walton_reach = bill_walton_height + 1 # assuming an extra foot for arm span
    if darth_vader_reach + rim_height > bill_walton_reach:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())