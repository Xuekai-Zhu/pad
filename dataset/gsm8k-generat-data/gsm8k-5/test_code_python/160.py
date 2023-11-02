def solution():
    # Calculate the cost of burgers
    burgers_cost = 100 * 3

    # Calculate the total cost of condiments and propane
    other_cost = 80

    # Calculate the total cost of the party, split equally among 4 people
    total_cost = (burgers_cost + other_cost + 200) / 4

    # Calculate how much John spent altogether
    john_spent = total_cost + 200

    result = john_spent
    return result

print(solution())