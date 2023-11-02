def solution():
    # Let's assume Carla's current age is x
    # Then, in 6 years, Carla will be 30: x + 6 = 30
    # Solving for x, we get Carla's current age as 24
    carla_age = 24

    # The sum of their current ages is 55: x + (x + L) = 55, where L is Louis's age.
    # Substituting x = 24, we get Louis's age as 7.
    louis_age = 31 - carla_age
    result = louis_age
    return result

print(solution())