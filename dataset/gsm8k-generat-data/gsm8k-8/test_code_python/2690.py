def solution():
    # Define the number of apples Bonnie bought
    bonnie_apples = 8

    # Calculate the number of apples Samuel bought
    samuel_apples = bonnie_apples + 20

    # Calculate the number of apples Samuel has left after eating half of them
    samuel_apples_left = samuel_apples / 2

    # Calculate the number of apples Samuel used to make apple pie
    apples_for_pie = samuel_apples / 7

    # Calculate the total number of apples Samuel has left
    total_apples_left = samuel_apples_left - apples_for_pie
    result = total_apples_left
    return result

print(solution())