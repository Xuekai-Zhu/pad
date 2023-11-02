def solution():
    # Calculate the total number of peppers previously purchased
    previous_total_peppers = 30*3 + 30*2 + 10*1

    # Calculate the total number of peppers currently purchased
    current_total_peppers = 15*2 + 90*1

    # Calculate the difference in peppers purchased
    difference_peppers = previous_total_peppers - current_total_peppers
    result = difference_peppers
    return result

print(solution())