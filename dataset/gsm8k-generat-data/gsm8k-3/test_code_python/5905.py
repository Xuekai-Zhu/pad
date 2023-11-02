def solution():
    """A vegan restaurant serves three kinds of protein: seitan, beans, and lentils. There are ten dishes on their menu. Two have beans and lentils, and two have beans and seitan. The remaining dishes only have one kind of protein in them. Half of the remaining dishes have only beans, and there are three times as many dishes with only beans as with only seitan. How many dishes include lentils?"""
    # Define the number of dishes on the menu
    NUM_DISHES = 10

    # Define the number of dishes with beans and lentils
    beans_lentils = 2

    # Define the number of dishes with beans and seitan
    beans_seitan = 2

    # Calculate the remaining number of dishes
    remaining_dishes = NUM_DISHES - beans_lentils - beans_seitan

    # Calculate the number of dishes with only beans
    beans_only = remaining_dishes // 2

    # Calculate the number of dishes with only seitan
    seitan_only = beans_only // 3

    # Calculate the number of dishes with only lentils
    lentils_only = remaining_dishes - beans_only - seitan_only

    # Calculate the total number of dishes with lentils
    total_lentils = beans_lentils + lentils_only
    
    # Display the total number of dishes with lentils
    result = total_lentils
    return result

print(solution())