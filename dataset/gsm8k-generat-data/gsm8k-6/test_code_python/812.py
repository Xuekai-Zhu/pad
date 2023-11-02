def solution():
    # Calculate the total number of candy pieces caught by Tabitha and her friends
    tabitha_candy = 22
    julie_candy = tabitha_candy / 2  # Julie caught half the amount of candy as Tabitha caught
    stan_candy = 13
    carlos_candy = 2 * stan_candy  # Carlos caught twice as much candy as Stan
    total_candy = tabitha_candy + julie_candy + stan_candy + carlos_candy
    result = total_candy
    return result

print(solution())