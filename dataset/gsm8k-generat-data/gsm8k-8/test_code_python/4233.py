def solution():
    # Define the number of people and amount of potatoes needed
    num_people = 40
    potatoes_needed = 1.5 * num_people

    # Calculate the number of bags of potatoes needed 
    bags_needed = potatoes_needed / 20

    # Calculate the cost of the bags of potatoes needed
    cost = bags_needed * 5

    result = cost
    return result

print(solution())