def solution():
    budget = 320  # Sally has a budget of $320
    book_cost = 12  # A reading book costs $12
    num_students = 30  # There are 30 students in Sally's class

    # Calculate the total cost of buying a reading book for every student
    total_cost = book_cost * num_students

    # Check if the budget is enough to cover the total cost
    if total_cost <= budget:
        result = 0  # Sally doesn't need to pay anything out of pocket
    else:
        result = total_cost - budget  # Sally needs to pay the difference out of pocket

    return result

print(solution())