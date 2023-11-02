def solution():
    num_students = 30
    valentiine_percentage = 0.6
    valentiine_cost = 2
    total_money = 40

    # Calculate the number of students who will receive valentine's cards
    num_valentines = num_students * valentiine_percentage

    # Calculate the total cost of all valentine's cards
    total_valentines_cost = num_valentines * valentiine_cost

    # Calculate the percentage of Mo's money that will be spent on valentine's cards
    percentage_spent_on_valentines = (total_valentines_cost / total_money) * 100
    result = percentage_spent_on_valentines
    return result

print(solution())