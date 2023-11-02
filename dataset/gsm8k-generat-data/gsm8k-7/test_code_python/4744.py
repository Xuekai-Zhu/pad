def solution():
    linemen = 12
    lineman_oz = 8
    skill_players = 10
    skill_oz = 6
    total_oz = 126

    # Calculate the total ounces used by the linemen
    linemen_oz = linemen * lineman_oz

    # Subtract the linemen's ounces from the total
    remaining_oz = total_oz - linemen_oz

    # Calculate the number of skill position players that can drink
    skill_players_drinking = remaining_oz // skill_oz

    # Calculate the number of skill position players that must wait for the cooler to refill
    waiting_players = skill_players - skill_players_drinking
    result = waiting_players
    return result

print(solution())