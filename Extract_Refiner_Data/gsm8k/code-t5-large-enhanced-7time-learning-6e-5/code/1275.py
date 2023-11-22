def solution():
    
    # Define the cost of each type of place setting
    DINNER_PLATE_PRICE = 6
    SALAD_PLATE_PRICE = 4

    # Define the number of people Avery is having over for dinner
    num_people = 12

    # Calculate the total cost of the dinner plates
    dinner_cost = num_people * DINNER_PLATE_PRICE

    # Calculate the total cost of the bowls
    bowl_cost = num_people * BOWL_PRICE

    # Calculate the total cost of the salad plates
    salad_cost = num_people * SALAD_PLATE_PRICE

    # Calculate the total cost of all the place settings
    total_cost = dinner_cost + bowl_cost + salad_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())