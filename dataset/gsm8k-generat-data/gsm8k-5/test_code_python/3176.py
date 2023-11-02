def solution():
    # Let's represent Matthew's age as x
    x = 0

    # Rebecca's age is 2 years younger than Matthew
    rebecca_age = x - 2

    # Freddy's age is 4 years older than Matthew
    freddy_age = x + 4

    # The sum of their ages is 35, so we can set up an equation
    # x + rebecca_age + freddy_age = 35
    # Substituting Rebecca and Freddy's ages in terms of x
    # x + (x-2) + (x+4) = 35
    # Simplifying the equation
    3x + 2 = 35

    # Solving for x, which represents Matthew's age
    x = (35 - 2) / 3

    # Matthew's age is 11
    # Freddy's age is 4 years older than Matthew, so he is 15 years old
    result = 15
    return result

print(solution())