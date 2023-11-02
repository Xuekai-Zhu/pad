def solution():
    # Define the number of main and minor characters
    main_characters = 5
    minor_characters = 4

    # Calculate the total cost for the minor characters
    minor_cost = minor_characters * 15000

    # Calculate the cost for each main character (three times the cost of a minor character)
    main_cost = 3 * 15000

    # Calculate the total cost for the main characters
    main_total_cost = main_characters * main_cost

    # Calculate the total cost per episode
    total_cost = minor_cost + main_total_cost
    result = total_cost
    return result

print(solution())