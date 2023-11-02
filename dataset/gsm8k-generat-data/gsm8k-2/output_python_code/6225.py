def solution():
    """At Theo’s cafe, he makes 3 egg and 4 egg omelettes. His cafe is open from 7:00 a.m. to 11:00 a.m. In the first hour, 5 customers order the 3 egg omelettes. In the second hour, 7 customers order the 4 egg omelettes. In the third hour, 3 customers order the 3 egg omelettes. In the last hour, 8 customers order the 4 egg omelettes. How many eggs does Theo need to make all the omelettes?"""
    hour1_eggs = 5 * 3
    hour2_eggs = 7 * 4
    hour3_eggs = 3 * 3
    hour4_eggs = 8 * 4
    total_eggs = hour1_eggs + hour2_eggs + hour3_eggs + hour4_eggs
    result = total_eggs
    return result

print(solution())