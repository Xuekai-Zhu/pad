def solution():
    """Henry has 30 more lollipops than Alison does. With 60 lollipops, Alisson has half the number of lollipops Diane has. If they combine the lollipops and eat 45 lollipops each day, calculate the total number of days it will take for them to finish the lollipops."""
    alison_lollipops = 60
    henry_lollipops = alison_lollipops + 30
    diane_lollipops = alison_lollipops * 2
    total_lollipops = alison_lollipops + henry_lollipops + diane_lollipops
    days_to_finish = total_lollipops // (45*3)
    result = days_to_finish
    return result

print(solution())