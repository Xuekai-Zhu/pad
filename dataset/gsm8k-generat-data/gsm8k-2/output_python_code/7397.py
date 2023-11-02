def solution():
    """A boy squirrel gathers 6 walnuts and carries them to his burrow in the tree, adding to the 12 already there, and dropping 1 on the way. The girl squirrel brings 5 more walnuts to their burrow and eats 2. How many walnuts are left?"""
    boy_squirrel_walnuts = 6
    girl_squirrel_walnuts = 5
    initial_walnuts = 12
    dropped_walnuts = 1
    eaten_walnuts = 2

    total_walnuts = initial_walnuts + boy_squirrel_walnuts + girl_squirrel_walnuts - dropped_walnuts - eaten_walnuts
    result = total_walnuts
    return result

print(solution())