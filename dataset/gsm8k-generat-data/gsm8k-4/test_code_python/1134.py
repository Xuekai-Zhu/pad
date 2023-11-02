def solution():
    """Henry has 30 more lollipops than Alison does. With 60 lollipops, Alisson has half the number of lollipops Diane has. If they combine the lollipops and eat 45 lollipops each day, calculate the total number of days it will take for them to finish the lollipops."""
    # Calculate the number of lollipops Alison has
    alison_lollipops = 60

    # Calculate the number of lollipops Henry has
    henry_lollipops = alison_lollipops + 30

    # Calculate the total number of lollipops
    total_lollipops = alison_lollipops + henry_lollipops

    # Calculate the number of lollipops Diane has
    diane_lollipops = alison_lollipops * 2

    # Calculate the total number of days it will take to finish the lollipops
    total_days = (total_lollipops - diane_lollipops) / (45 * 2)

    result = total_days
    return result

print(solution())