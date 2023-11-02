def solution():
    # Calculate the initial number of supplies Kelly had
    initial_paper = 8 * 3  # 8 students need 3 pieces of construction paper each
    initial_glue = 6  # 6 bottles of glue
    initial_supplies = initial_paper + initial_glue  # total initial supplies

    # Calculate the number of supplies left after Kelly dropped half of them down the storm drain
    remaining_supplies = initial_supplies // 2  # dropped half of the initial supplies

    # Calculate the number of supplies left after Kelly bought 5 more pieces of construction paper
    remaining_paper = initial_paper - (initial_paper // 2) + 5  # half of the initial paper was lost, but Kelly bought 5 more
    remaining_supplies += remaining_paper  # add remaining paper to remaining supplies
    remaining_supplies += initial_glue  # add initial glue to remaining supplies

    result = remaining_supplies
    return result

print(solution())