def solution():
    # Calculate the number of roses in Claire's garden
    roses = 400 - 120  # the rest of the flowers are roses

    # Calculate the number of red roses and the amount earned by selling half of them
    red_roses = roses - 80  # the rest of the roses are red
    amount_earned = 0.5 * red_roses * 0.75  # each red rose is worth $0.75

    result = amount_earned
    return result

print(solution())