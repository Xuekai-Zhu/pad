def solution():
    budget = 320
    book_cost = 12
    num_students = 30

    # Calculate the total cost of books needed for all students
    total_book_cost = book_cost * num_students

    # Check if the budget is enough to cover the total book cost
    if total_book_cost <= budget:
        return 0  # Sally doesn't need to pay out of pocket

    # Calculate the amount Sally needs to pay out of pocket
    extra_cost = total_book_cost - budget
    result = extra_cost
    return result

print(solution())