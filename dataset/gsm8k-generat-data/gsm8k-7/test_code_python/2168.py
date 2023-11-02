def solution():
    raised_funds = 10000
    friends_percent = 0.4
    family_percent = 0.3

    # Calculate the amount raised by friends
    friends_funds = raised_funds * friends_percent

    # Calculate the amount remaining after friends' contribution
    remaining_funds = raised_funds - friends_funds

    # Calculate the amount raised by family
    family_funds = remaining_funds * family_percent

    # Calculate the amount saved by the president
    president_funds = raised_funds - friends_funds - family_funds
    result = president_funds
    return result

print(solution())