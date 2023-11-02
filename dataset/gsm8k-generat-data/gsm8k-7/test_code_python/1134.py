def solution():
    alison_lollipops = 60
    henry_lollipops = alison_lollipops + 30

    diane_lollipops = alison_lollipops * 2
    total_lollipops = alison_lollipops + henry_lollipops + diane_lollipops

    days_to_finish = total_lollipops // (45 * 3)
    result = days_to_finish
    return result

print(solution())