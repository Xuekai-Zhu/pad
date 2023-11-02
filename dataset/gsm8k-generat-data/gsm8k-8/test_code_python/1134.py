def solution():
    # Calculate the number of lollipops Henry has
    henry_lollipops = 60 + 30

    # Calculate the number of lollipops Diane has
    diane_lollipops = 2 * 60

    # Calculate the total number of lollipops
    total_lollipops = henry_lollipops + 60 + diane_lollipops

    # Calculate the number of days it will take to finish the lollipops
    days_to_finish = total_lollipops // (3 * 45)

    result = days_to_finish
    return result

print(solution())