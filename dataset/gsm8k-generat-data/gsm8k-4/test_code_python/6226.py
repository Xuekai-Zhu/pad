def solution():
    """At Theo’s cafe, he makes 3 egg and 4 egg omelettes. His cafe is open from 7:00 a.m. to 11:00 a.m. In the first hour, 5 customers order the 3 egg omelettes. In the second hour, 7 customers order the 4 egg omelettes. In the third hour, 3 customers order the 3 egg omelettes. In the last hour, 8 customers order the 4 egg omelettes. How many eggs does Theo need to make all the omelettes?"""
    
    # Define the number of eggs needed for each omelette
    eggs_3_omelette = 3
    eggs_4_omelette = 4

    # Define the number of orders for each type of omelette
    orders_3_1 = 5
    orders_4_2 = 7
    orders_3_3 = 3
    orders_4_4 = 8

    # Calculate the total number of eggs needed for each type of omelette
    eggs_3_1 = orders_3_1 * eggs_3_omelette
    eggs_4_2 = orders_4_2 * eggs_4_omelette
    eggs_3_3 = orders_3_3 * eggs_3_omelette
    eggs_4_4 = orders_4_4 * eggs_4_omelette

    # Calculate the total number of eggs needed
    total_eggs = eggs_3_1 + eggs_4_2 + eggs_3_3 + eggs_4_4

    # return the result
    result = total_eggs
    return result

print(solution())