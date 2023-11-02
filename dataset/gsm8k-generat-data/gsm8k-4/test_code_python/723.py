def solution():
    """John eats a bag of chips for dinner and then eats twice as many after dinner. How many bags of chips did he eat?"""
    # Define the number of bags of chips eaten for dinner
    dinner_chips = 1

    # Define the ratio of chips eaten after dinner to chips eaten for dinner
    after_dinner_ratio = 2

    # Calculate the number of bags of chips eaten after dinner
    after_dinner_chips = dinner_chips * after_dinner_ratio

    # Calculate the total number of bags of chips eaten
    total_chips = dinner_chips + after_dinner_chips

    # return the result
    result = total_chips
    return result

print(solution())