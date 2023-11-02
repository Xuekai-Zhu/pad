def solution():
    # Define the number of war supplies at Grenada Army Base
    grenada_war_supplies = 6000

    # Calculate the number of guns at Rockefeller Army Base
    rockefeller_guns = 2 * grenada_war_supplies + 3000

    # Calculate the number of war tractors at Rockefeller Army Base
    rockefeller_war_tractors = 3 * grenada_war_supplies - 400

    # Calculate the number of soldier uniforms at Rockefeller Army Base
    rockefeller_soldier_uniforms = 30 * grenada_war_supplies

    # Calculate the total number of war supplies at Rockefeller Army Base
    total_war_supplies = rockefeller_guns + rockefeller_war_tractors + rockefeller_soldier_uniforms
    result = total_war_supplies
    return result

print(solution())