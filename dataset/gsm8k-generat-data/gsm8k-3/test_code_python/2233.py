def solution():
    """Jorge and Giuliana each eat 7 croissants for breakfast, 18 cakes after school, and 30 pizzas before bedtime. What is the total number of croissants, cakes, and pizzas the two consume in a day?"""
    # Define the number of croissants, cakes, and pizzas each person eats
    CROISSANTS_PER_PERSON = 7
    CAKES_PER_PERSON = 18
    PIZZAS_PER_PERSON = 30

    # Calculate the total number of croissants, cakes, and pizzas consumed
    total_croissants = CROISSANTS_PER_PERSON * 2
    total_cakes = CAKES_PER_PERSON * 2
    total_pizzas = PIZZAS_PER_PERSON * 2
    total_consumed = total_croissants + total_cakes + total_pizzas

    # Display the total number of croissants, cakes, and pizzas consumed
    result = total_consumed
    return result

print(solution())