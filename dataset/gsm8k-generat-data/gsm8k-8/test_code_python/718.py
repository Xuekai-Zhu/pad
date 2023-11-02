def solution():
    # Define the length of Jenny's snake
    jenny_length = x

    # Calculate the length of Jake's snake
    jake_length = jenny_length + 12

    # Calculate the total length of the snakes
    total_length = jenny_length + jake_length

    # Solve for jenny_length using the equation total_length = 70 inches
    jenny_length = (70 - 12) / 2

    # Calculate Jake's length using the equation jake_length = jenny_length + 12
    jake_length = jenny_length + 12
    result = jake_length
    return result

print(solution())