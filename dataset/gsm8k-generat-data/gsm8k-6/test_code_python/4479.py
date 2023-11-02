def solution():
    # Calculate the total number of ears of corn given away
    total_given_away = 8 + 3 + 12 + 21*14  # Terry took 8, Jerry took 3, Linda took 12, Stacy took 21 bushels (21*14 ears in a bushel)

    # Calculate the number of ears of corn Bob has left
    ears_left = 50*14 - total_given_away  # 50 bushels of corn with 14 ears per bushel minus the total given away
    result = ears_left
    return result

print(solution())