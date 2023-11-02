def solution():
    # Define the cost of the book set
    book_cost = 150

    # Calculate the total area of the lawns she has already mowed
    area_mowed = 3 * 20 * 15

    # Calculate the amount of money she has made so far
    money_made = area_mowed * 0.1

    # Calculate the remaining amount of money she needs to earn for the book set
    remaining_money = book_cost - money_made

    # Calculate the remaining square footage she needs to mow
    remaining_area = remaining_money / 0.1
    result = remaining_area
    return result

print(solution())