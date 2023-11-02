def solution():
    # Calculate the total prize money available for fourth place onwards
    remaining_money = 800 - 200 - 150 - 120

    # Calculate how many writers will receive a share of the remaining money
    writers_remaining = 18 - 3

    # Calculate how much each writer will earn
    each_writer_earnings = remaining_money / writers_remaining
    result = each_writer_earnings
    return result

print(solution())