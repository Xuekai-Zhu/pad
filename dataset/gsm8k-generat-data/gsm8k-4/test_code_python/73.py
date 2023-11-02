def solution():
    """It is Roger’s turn to provide a snack for the baseball team after the game and he has decided to bring trail mix. The trail mix comes in packs of 6 individual pouches. Roger has 13 members on his baseball team, plus 3 coaches and 2 helpers. How many packs of trail mix does he need to buy?"""
    # Define the number of people on the baseball team
    team_size = 13

    # Define the number of coaches and helpers
    others = 3 + 2

    # Calculate the total number of people to provide snack for
    total_people = team_size + others

    # Calculate the number of packs of trail mix needed
    packs_needed = total_people // 6 + (total_people % 6 > 0)

    # return the result
    result = packs_needed
    return result

print(solution())