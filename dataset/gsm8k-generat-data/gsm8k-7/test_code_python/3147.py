def solution():
    parakeet_daily_need = 2
    parrot_daily_need = 14
    finch_daily_need = parakeet_daily_need / 2  # half of what a parakeet eats

    num_parakeets = 3
    num_parrots = 2
    num_finches = 4

    total_weekly_need = (parakeet_daily_need * num_parakeets) + (parrot_daily_need * num_parrots) + (
                finch_daily_need * num_finches)

    # Calculate the total amount of birdseed needed in grams for a week
    weekly_need_grams = total_weekly_need * 7
    result = weekly_need_grams
    return result

print(solution())