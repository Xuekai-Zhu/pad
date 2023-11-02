def solution():
    total_prize_money = 800  # The publishing house will award a total of $800 in prizes
    first_place = 200  # First place will get $200
    second_place = 150  # Second place will get $150
    third_place = 120  # Third place will get $120
    remaining_places = 15  # There are 18 novels with the most votes, and 3 have already been awarded

    # Calculate the total amount of money awarded to the remaining places
    remaining_prize_money = total_prize_money - first_place - second_place - third_place
    # Calculate the amount of money each writer will earn from fourth place onwards
    each_writer_earns = remaining_prize_money / remaining_places
    result = each_writer_earns
    return result

print(solution())