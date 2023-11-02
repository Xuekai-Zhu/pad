def solution():
    pounds_lost_so_far = 3 + 4  # Michael has already lost 3 pounds in March and 4 pounds in April
    pounds_to_lose = 10 - pounds_lost_so_far  # Michael wants to lose a total of 10 pounds by June
    pounds_to_lose_in_May = pounds_to_lose / 1  # There is 1 month (May) left to lose the remaining pounds

    result = pounds_to_lose_in_May
    return result

print(solution())