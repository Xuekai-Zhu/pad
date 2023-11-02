def solution():
    # Calculate the number of students receiving a Valentine
    students_with_valentine = round(0.6 * 30)

    # Calculate the total cost of the cards
    total_cost = 2 * students_with_valentine

    # Calculate the percentage of Mo's money spent on Valentine
    percentage_spent = (total_cost / 40) * 100
    result = percentage_spent
    return result

print(solution())