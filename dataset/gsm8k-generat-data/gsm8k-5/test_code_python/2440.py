def solution():
    # Calculate the total number of tickets Wally gives away
    tickets_given = (3/4) * 400

    # Calculate the total ratio of tickets shared by Jensen and Finley
    total_ratio = 4 + 11

    # Calculate Finley's share of the tickets based on the ratio
    finley_share = (11/total_ratio) * tickets_given

    result = finley_share
    return result

print(solution())