def solution():
    """Henry has 30 more lollipops than Alison does. With 60 lollipops, Alisson has half the number of lollipops Diane has. If they combine the lollipops and eat 45 lollipops each day, calculate the total number of days it will take for them to finish the lollipops."""
    alison_lollipops = 60
    diane_lollipops = alison_lollipops * 2
    henry_lollipops = alison_lollipops + 30
    total_lollipops = alison_lollipops + diane_lollipops + henry_lollipops
    days = total_lollipops // (45 * 3)
    result = days
    return result

print(solution())