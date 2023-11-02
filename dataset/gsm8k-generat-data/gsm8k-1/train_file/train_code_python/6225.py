def solution():
    """At Theo’s cafe, he makes 3 egg and 4 egg omelettes. His cafe is open from 7:00 a.m. to 11:00 a.m. In the first hour, 5 customers order the 3 egg omelettes. In the second hour, 7 customers order the 4 egg omelettes. In the third hour, 3 customers order the 3 egg omelettes. In the last hour, 8 customers order the 4 egg omelettes. How many eggs does Theo need to make all the omelettes?"""
    eggs_per_3_omelette = 3
    eggs_per_4_omelette = 4
    hour1_orders = 5
    hour2_orders = 7
    hour3_orders = 3
    hour4_orders = 8
    total_3_omelettes = hour1_orders + hour3_orders
    total_4_omelettes = hour2_orders + hour4_orders
    total_eggs = (total_3_omelettes * eggs_per_3_omelette) + (total_4_omelettes * eggs_per_4_omelette)
    result = total_eggs
    return result

print(solution())