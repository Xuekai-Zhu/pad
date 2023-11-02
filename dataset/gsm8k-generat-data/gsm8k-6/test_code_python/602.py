def solution():
    # Calculate the total amount of money to be distributed to the 18 novels
    total_money = 800
    first_place = 200
    second_place = 150
    third_place = 120
    remaining_awards = total_money - (first_place + second_place + third_place)

    # Calculate the amount of money each writer will earn from fourth place onwards
    num_writers = 18 - 3  # subtracting the top 3 places
    each_writer_earn = remaining_awards / num_writers
    result = each_writer_earn
    return result

print(solution())