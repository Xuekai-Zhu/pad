def solution():
    crates_on_tuesday = 6  # Michael bought 6 crates on Tuesday
    crates_given_away = 2  # Michael gave 2 crates away to Susan
    crates_on_thursday = 5  # Michael bought 5 more crates on Thursday

    # Calculate the total number of crates Michael has now
    total_crates = crates_on_tuesday - crates_given_away + crates_on_thursday

    # Calculate the total number of eggs Michael has now
    eggs = total_crates * 30  # One crate holds 30 eggs

    result = eggs
    return result

print(solution())