def solution():
    tabitha_candy = 22  # Tabitha caught 22 pieces of candy
    stan_candy = 13  # Stan caught 13 pieces of candy
    julie_candy = tabitha_candy // 2  # Julie caught half the amount of candy Tabitha caught
    carlos_candy = 2 * stan_candy  # Carlos caught twice the amount of candy Stan caught

    # Calculate the total number of candy caught by the friends
    total_candy = tabitha_candy + stan_candy + julie_candy + carlos_candy
    result = total_candy
    return result

print(solution())