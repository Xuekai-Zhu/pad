def solution():
    num_sheep = 400

    # Calculate the number of sheep given to sister
    sheep_to_sister = num_sheep / 4

    # Calculate the remaining number of sheep
    remaining_sheep = num_sheep - sheep_to_sister

    # Calculate the number of sheep given to brother
    sheep_to_brother = remaining_sheep / 2

    # Calculate the final number of sheep remaining with Mary
    final_sheep = remaining_sheep - sheep_to_brother

    result = final_sheep
    return result

print(solution())