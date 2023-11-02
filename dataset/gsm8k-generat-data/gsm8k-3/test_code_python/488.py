def solution():
    """Mrs. Smith wanted to buy wears worth $500. She went to a boutique with the $500 but by the time she had picked out everything
    she liked, she realized that she would need two-fifths more money than she had. If the shop owner gave her a discount of 15%,
    how much more money will she still need?"""
    # initial amount Mrs. Smith went to the boutique with
    initial_amount = 500

    # calculate the amount of money needed for two-fifths more than her initial amount
    additional_amount = initial_amount * (2 / 5)

    # calculate the total amount needed after adding the additional amount
    total_amount = initial_amount + additional_amount

    # calculate the discount received
    discount = total_amount * 0.15

    # calculate the final amount Mrs. Smith will need to pay
    final_amount = total_amount - discount

    # calculate the remaining amount Mrs. Smith will need to pay
    remaining_amount = final_amount - initial_amount

    # Display the remaining amount Mrs. Smith will need to pay
    result = remaining_amount
    return result

print(solution())