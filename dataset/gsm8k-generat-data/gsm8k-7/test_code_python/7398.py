def solution():
    boy_squirrel_walnuts = 6
    girl_squirrel_walnuts = 5
    starting_walnuts = 12
    dropped_walnuts = 1
    girl_squirrel_consumption = 2

    # Calculate the total number of walnuts after the boy squirrel adds his walnuts and drops one
    total_walnuts = starting_walnuts + boy_squirrel_walnuts - dropped_walnuts

    # Calculate the total number of walnuts after the girl squirrel brings her walnuts and eats some
    total_walnuts += girl_squirrel_walnuts - girl_squirrel_consumption

    result = total_walnuts
    return result

print(solution())