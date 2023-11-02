def solution():
    # Define the number of peppers picked each day
    sunday_peppers = 7
    monday_peppers = 12
    tuesday_peppers = 14
    wednesday_peppers = 12
    thursday_peppers = 5
    friday_peppers = 18
    saturday_peppers = 12

    # Calculate the total number of peppers picked
    total_peppers = sunday_peppers + monday_peppers + tuesday_peppers + wednesday_peppers + thursday_peppers + friday_peppers + saturday_peppers

    # Calculate the number of hot peppers picked
    hot_peppers = 0.2 * total_peppers

    # Calculate the number of non-hot peppers picked
    non_hot_peppers = total_peppers - hot_peppers

    result = non_hot_peppers
    return result

print(solution())