def solution():
    # Define the number of people and sacks lunches needed
    num_people = 35 + 5 + 1
    num_lunches = num_people + 3

    # Calculate the total cost of the lunches
    total_cost = num_lunches * 7

    result = total_cost
    return result

print(solution())