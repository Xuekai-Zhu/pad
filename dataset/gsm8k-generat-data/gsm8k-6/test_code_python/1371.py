def solution():
    # Calculate the amount of money Natalie gets
    natalie_share = 10000 / 2

    # Calculate the amount of money Rick gets
    rick_share = 0.6 * (10000 - natalie_share)

    # Calculate the amount of money Lucy gets
    lucy_share = 10000 - natalie_share - rick_share
    result = lucy_share
    return result

print(solution())