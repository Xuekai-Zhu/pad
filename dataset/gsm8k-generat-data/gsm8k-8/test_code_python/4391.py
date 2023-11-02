def solution():
    # Define the number of quarters and the cost of the dress
    quarters = 160
    dress_cost = 35

    # Calculate the number of quarters left after replacing the dress
    quarters_left = quarters - (dress_cost / 0.25)
    result = quarters_left
    return result

print(solution())