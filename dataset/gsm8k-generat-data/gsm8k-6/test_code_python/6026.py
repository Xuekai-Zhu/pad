def solution():
    # Calculate the total number of burritos John initially had
    total_burritos = 3 * 20  # 3 boxes of 20 burritos each

    # Calculate the number of burritos given away to his friend
    given_away = total_burritos / 3  # a third of the total

    # Calculate the number of burritos John ate
    ate = 3 * 10  # 3 burritos per day for 10 days

    # Calculate the number of burritos left
    left = total_burritos - given_away - ate

    result = left
    return result

print(solution())