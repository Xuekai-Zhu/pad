def solution():
    """Dean has 30 marbles. He gives 1/5 of them to Jamie and gives 10 to Donald. How many marbles are left for Dean?"""
    total_marbles = 30
    jamie_share = total_marbles / 5
    donald_share = 10
    remaining_marbles = total_marbles - jamie_share - donald_share
    result = remaining_marbles
    return result

print(solution())