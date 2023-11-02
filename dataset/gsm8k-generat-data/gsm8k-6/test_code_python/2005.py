def solution():
    # Calculate the total number of cups of lemonade that Hazel made
    cups_sold_to_kids = 18
    cups_given_to_friends = (1/2) * cups_sold_to_kids
    total_cups_sold = cups_sold_to_kids + cups_given_to_friends + 1  # sold half to construction crew, gave away half of the rest, drank the last cup
    result = total_cups_sold
    return result

print(solution())