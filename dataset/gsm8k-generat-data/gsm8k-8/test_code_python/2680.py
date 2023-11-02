def solution():
    research_time = 6 # months
    first_expedition_time = 2 # years (24 months)
    second_expedition_time = 3 * (research_time + first_expedition_time)

    total_time = research_time + first_expedition_time + second_expedition_time
    result = total_time
    return result

print(solution())