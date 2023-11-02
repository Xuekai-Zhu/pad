def solution():
    # Calculate the total cost of the movie tickets
    tickets_cost = 7 * 3

    # Calculate the cost of the popcorn
    popcorn_cost = 1.5 * 2

    # Calculate the cost of the milk tea
    milk_tea_cost = 3 * 3

    # Calculate the total expenses
    total_expenses = tickets_cost + popcorn_cost + milk_tea_cost

    # Calculate the per-person cost by dividing the total expenses by 3
    per_person_cost = total_expenses / 3

    result = per_person_cost
    return result

print(solution())