def solution():
    # Calculate the value of X and Y based on the information given
    value_X = 200 / 2  # X is tagged with half the number W is tagged with
    value_Y = 200 + value_X  # Y is tagged with the total of X and W's tags

    # Calculate the total of all the tagged numbers
    total = 200 + value_X + value_Y + 400  # W is tagged with 200, X is tagged with value_X, Y is tagged with value_Y, Z is tagged with 400
    result = total
    return result

print(solution())