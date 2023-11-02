def solution():
    dictionary_cost = 18  # The dictionary costs $18
    dinosaur_book_cost = 13  # The dinosaur book costs $13
    childrens_cookbook_cost = 8  # The children's cookbook costs $8
    saved_money = 14  # Tyler has saved $14 from his allowance
    hourly_rate = 5  # Tyler earns $5 per hour

    # Calculate the total cost of the books
    total_cost = dictionary_cost + dinosaur_book_cost + childrens_cookbook_cost

    # Calculate the number of hours Tyler needs to work to afford his books
    hours_needed = total_cost / hourly_rate
    result = hours_needed
    return result

print(solution())