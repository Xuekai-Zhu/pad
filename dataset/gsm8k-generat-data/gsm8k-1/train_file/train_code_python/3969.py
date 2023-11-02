def solution():
    """Carla adds a can of chilis, two cans of beans, and 50% more tomatoes than beans to a normal batch of chili. If she makes a quadruple batch, how many cans of food does she need?"""
    normal_tomatoes_per_batch = 2
    normal_beans_per_batch = 2
    normal_chilis_per_batch = 1
    tomatoes_per_batch = normal_beans_per_batch * 1.5
    total_tomatoes = tomatoes_per_batch * 4
    total_beans = normal_beans_per_batch * 2 * 4
    total_chilis = normal_chilis_per_batch * 4
    total_cans = total_tomatoes + total_beans + total_chilis
    result = total_cans
    return result

print(solution())