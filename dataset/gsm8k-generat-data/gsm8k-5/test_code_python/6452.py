def solution():
    initial_bottles = 10  # Elizabeth starts with 10 water bottles
    lost_at_school = 2  # Elizabeth loses 2 water bottles at school
    stolen_at_dance = 1  # Elizabeth has 1 water bottle stolen at dance practice

    remaining_bottles = initial_bottles - lost_at_school - stolen_at_dance  # Elizabeth has this many water bottles left
    stickers_per_bottle = 3  # Elizabeth puts 3 stickers on each remaining water bottle

    # Calculate the total number of stickers Elizabeth uses
    total_stickers = remaining_bottles * stickers_per_bottle
    result = total_stickers
    return result

print(solution())