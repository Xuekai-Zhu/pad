def solution():
    w = 200  # W is tagged with the number 200
    x = 0.5 * w  # X is tagged with half the number W is tagged with
    y = x + w  # Y is tagged with the total of X and W's tags
    z = 400  # Z is tagged with the number 400

    # Calculate the total of all the tagged numbers
    total = w + x + y + z
    result = total
    return result

print(solution())