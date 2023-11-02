def solution():
    total_prize = 800
    first_place_prize = 200
    second_place_prize = 150
    third_place_prize = 120
    num_other_awards = 18 - 3

    # Calculate the total amount of money for the rest of the awards
    other_awards_money = total_prize - first_place_prize - second_place_prize - third_place_prize

    # Calculate the amount of money for each writer from fourth place onwards
    money_per_writer = other_awards_money / num_other_awards
    result = money_per_writer
    return result

print(solution())