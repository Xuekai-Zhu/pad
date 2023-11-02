def solution():
    # Calculate the initial amount of walnuts in the burrow
    initial_amount = 12

    # Calculate the number of walnuts the boy squirrel brought
    boy_squirrel = 6

    # Calculate the number of walnuts the girl squirrel brought and ate
    girl_squirrel = 5
    girl_squirrel_eaten = 2

    # Calculate the total number of walnuts
    total_walnuts = initial_amount + boy_squirrel + girl_squirrel - girl_squirrel_eaten - 1

    result = total_walnuts
    return result

print(solution())