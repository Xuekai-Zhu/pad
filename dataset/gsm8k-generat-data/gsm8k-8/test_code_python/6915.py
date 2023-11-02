def solution():
    # Define the fractions of players in each age group
    between_25_35 = 2/5
    older_than_35 = 3/8

    # Calculate the fraction of players younger than 25
    younger_than_25 = 1 - between_25_35 - older_than_35

    # Calculate the number of players in each age group
    total_players = 1000
    between_25_35_count = between_25_35 * total_players
    older_than_35_count = older_than_35 * total_players
    younger_than_25_count = younger_than_25 * total_players

    # Calculate the number of players younger than 25
    result = younger_than_25_count
    return result

print(solution())