def solution():
    # Define the variables
    total_yarn = 10
    number_of_parts = 5
    parts_used = 3

    # Calculate the length of each part
    part_length = total_yarn / number_of_parts

    # Calculate the length of the yarn used for crocheting
    yarn_used = parts_used * part_length
    result = yarn_used
    return result

print(solution())