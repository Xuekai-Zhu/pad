def solution():
    total_prize_money = 200  # Bob won 100 dollars in the first two weeks
    puppy_cost = 1000

    # Calculate how much additional prize money Bob needs to save up for the puppy
    remaining_money_needed = puppy_cost - total_prize_money

    # Calculate the minimum number of additional weeks Bob needs to win first place
    additional_weeks_needed = remaining_money_needed // 100 + (remaining_money_needed % 100 > 0)
    result = additional_weeks_needed
    return result

print(solution())