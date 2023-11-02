def solution():
    # Initial population
    weasels = 100
    rabbits = 50

    # Population after 3 weeks of hunting
    weasels -= 3 * 4 * 3  # 3 foxes catch 4 weasels per week for 3 weeks
    rabbits -= 3 * 2 * 3  # 3 foxes catch 2 rabbits per week for 3 weeks

    result = f"After 3 weeks, there will be {weasels} weasels and {rabbits} rabbits left."
    return result

print(solution())