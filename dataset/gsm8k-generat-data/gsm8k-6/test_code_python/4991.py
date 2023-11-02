def solution():
    # Calculate the number of boys and girls in the school
    num_boys = 0.6 * 200
    num_girls = 0.4 * 200

    # Calculate the number of votes June needs to win
    votes_needed = 0.51 * 200

    # Calculate the number of votes she has from boys
    votes_from_boys = 0.675 * num_boys

    # Calculate the number of votes she needs from girls
    votes_needed_from_girls = votes_needed - votes_from_boys

    # Calculate the percentage of votes she needs from girls
    percentage_needed_from_girls = (votes_needed_from_girls / num_girls) * 100
    result = percentage_needed_from_girls
    return result

print(solution())