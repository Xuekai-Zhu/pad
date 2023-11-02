def solution():
    alison_lollipops = 60  # Alison has 60 lollipops
    henry_lollipops = alison_lollipops + 30  # Henry has 30 more lollipops than Alison
    total_lollipops = alison_lollipops + henry_lollipops  # Total number of lollipops

    # Calculate the number of lollipops Diane has
    diane_lollipops = alison_lollipops * 2

    # Calculate the total number of lollipops they will eat
    total_eaten = 45 * 3  # Each of them eats 45 lollipops per day, and there are 3 of them

    # Calculate the number of days it will take to finish the lollipops
    days_to_finish = total_lollipops / total_eaten

    result = days_to_finish
    return result

print(solution())