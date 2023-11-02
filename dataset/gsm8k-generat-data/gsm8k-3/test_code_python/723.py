def solution():
    """John eats a bag of chips for dinner and then eats twice as many after dinner.  How many bags of chips did he eat?"""
    # Define the number of bags eaten for dinner
    dinner_bags = 1

    # Define the multiplier for the number of bags eaten after dinner
    after_dinner_multiplier = 2

    # Calculate the number of bags eaten after dinner
    after_dinner_bags = dinner_bags * after_dinner_multiplier

    # Calculate the total number of bags eaten
    total_bags = dinner_bags + after_dinner_bags
    
    # Display the total number of bags eaten
    result = total_bags
    return result

print(solution())