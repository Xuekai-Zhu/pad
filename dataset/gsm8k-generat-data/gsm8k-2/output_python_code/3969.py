def solution():
    """Carla adds a can of chilis, two cans of beans, and 50% more tomatoes than beans to a normal batch of chili. If she makes a quadruple batch, how many cans of food does she need?"""
    normal_chilis = 1
    normal_beans = 2
    normal_tomatoes = normal_beans * 1.5
    quadruple_chilis = normal_chilis * 4
    quadruple_beans = normal_beans * 4 * 2
    quadruple_tomatoes = normal_tomatoes * 4 * 1.5
    total_cans = quadruple_chilis + quadruple_beans + quadruple_tomatoes
    result = total_cans
    return result

print(solution())