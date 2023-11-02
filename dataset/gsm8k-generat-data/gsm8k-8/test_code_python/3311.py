def solution():
    # Calculate the amount he made on his most recent painting
    current_sale = 44000

    # Calculate the value of five times more than the previous painting
    five_times_previous = current_sale + 1000
    previous_sale = (five_times_previous / 5)

    # Return the value of the previous sale
    result = previous_sale
    return result

print(solution())