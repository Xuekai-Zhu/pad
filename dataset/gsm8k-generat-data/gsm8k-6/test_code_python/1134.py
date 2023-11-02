def solution():
    alison_lollipops = 60  # given
    henry_lollipops = alison_lollipops + 30  # Henry has 30 more lollipops than Alison
    diane_lollipops = alison_lollipops * 2  # Alisson has half the number of lollipops Diane has
    total_lollipops = alison_lollipops + henry_lollipops + diane_lollipops
    days_to_finish = total_lollipops // (45 * 3)  # they eat 45 lollipops each day
    result = days_to_finish
    return result

print(solution())