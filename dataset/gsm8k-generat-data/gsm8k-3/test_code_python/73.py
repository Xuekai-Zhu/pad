def solution():
    """It is Roger’s turn to provide a snack for the baseball team after the game and he has decided to bring trail mix. The trail mix comes in packs of 6 individual pouches. Roger has 13 members on his baseball team, plus 3 coaches and 2 helpers. How many packs of trail mix does he need to buy?"""
    # Define the number of members on the team, coaches, and helpers
    members = 13
    coaches = 3
    helpers = 2

    # Calculate the total number of people
    total_people = members + coaches + helpers

    # Calculate the number of packs of trail mix needed
    packs_needed = total_people // 6
    if total_people % 6 != 0:
        packs_needed += 1

    result = packs_needed
    return result

print(solution())