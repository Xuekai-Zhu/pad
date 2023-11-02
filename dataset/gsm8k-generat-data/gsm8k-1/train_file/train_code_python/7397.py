def solution():
    """A boy squirrel gathers 6 walnuts and carries them to his burrow in the tree, adding to the 12 already there, and dropping 1 on the way. The girl squirrel brings 5 more walnuts to their burrow and eats 2. How many walnuts are left?"""
    boy_walnuts = 6
    girl_walnuts = 5
    walnuts_dropped = 1
    walnuts_eaten = 2
    total_walnuts = (boy_walnuts + girl_walnuts + 12) - walnuts_dropped - walnuts_eaten
    result = total_walnuts
    return result

print(solution())