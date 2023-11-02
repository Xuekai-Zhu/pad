def solution():
    # Calculate the total cost of the hamburgers
    hamburgers_cost = 5 * 3

    # Calculate the total cost of the French fries
    fries_cost = 4 * 1.2

    # Calculate the total cost of the soda
    soda_cost = 5 * 0.5

    # Calculate the total cost of the spaghetti
    spaghetti_cost = 2.7

    # Calculate the total cost of all the food
    total_cost = hamburgers_cost + fries_cost + soda_cost + spaghetti_cost

    # Calculate how much each person should pay
    num_people = 5
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())