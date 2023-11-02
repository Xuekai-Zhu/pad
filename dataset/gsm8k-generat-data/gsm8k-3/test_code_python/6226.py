def solution():
    """At Theo’s cafe, he makes 3 egg and 4 egg omelettes.  His cafe is open from 7:00 a.m. to 11:00 a.m.  
    In the first hour, 5 customers order the 3 egg omelettes.  In the second hour, 7 customers order the 4 egg omelettes.  
    In the third hour, 3 customers order the 3 egg omelettes. In the last hour, 8 customers order the 4 egg omelettes.
    How many eggs does Theo need to make all the omelettes?"""
    
    # Define the number of eggs needed for each type of omelette
    EGG_3_OMLETTE = 3
    EGG_4_OMLETTE = 4

    # Define the number of orders of each type of omelette in each hour
    hour1_3egg = 5
    hour1_4egg = 0
    hour2_3egg = 0
    hour2_4egg = 7
    hour3_3egg = 3
    hour3_4egg = 0
    hour4_3egg = 0
    hour4_4egg = 8

    # Calculate the total number of eggs needed for each type of omelette
    total_eggs_3egg = hour1_3egg + hour3_3egg
    total_eggs_4egg = hour2_4egg + hour4_4egg

    # Calculate the total number of eggs needed for all omelettes
    total_eggs = (total_eggs_3egg * EGG_3_OMLETTE) + (total_eggs_4egg * EGG_4_OMLETTE)

    # Display the total number of eggs needed
    result = total_eggs
    return result

print(solution())