def solution():
    starting_money = 40
    num_quarters = 200
    money_given_to_sister = 5
    quarters_given_to_sister = 120

    # Calculate the total value of the quarters
    quarters_value = num_quarters * 0.25

    # Calculate the total value of the money before giving any to his sister
    total_value_before = starting_money + quarters_value

    # Calculate the total value of the money and quarters given to his sister
    total_given = money_given_to_sister + (quarters_given_to_sister * 0.25)

    # Calculate the total value of the money left after giving to his sister
    total_left = total_value_before - total_given
    result = total_left
    return result

print(solution())