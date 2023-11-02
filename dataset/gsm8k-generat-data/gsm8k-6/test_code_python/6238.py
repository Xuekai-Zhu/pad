def solution():
    # Calculate the total expenses
    total_expenses = (7 * 3) + (1.5 * 2) + (3 * 3)  # Mitch paid for the tickets at $7 each, Jam paid for 2 boxes of popcorn at $1.5 each, Jay paid for 3 cups of milk tea at $3 each
    number_of_people = 3  # three friends split the total expenses
    each_should_contribute = total_expenses / number_of_people 
    result = each_should_contribute
    return result

print(solution())