def solution():
    """Jade had $38 and her sister Julia had half as much money she had. On New Year's eve, their aunt gave each of them an equal amount of money so that they had a total of $97. How much did their aunt give each of them?"""
    # Define Jade's initial amount of money
    jade_money = 38

    # Define Julia's initial amount of money
    julia_money = jade_money / 2

    # Define the total amount of money they had after their aunt gave them money
    total_money = 97

    # Calculate the amount of money their aunt gave each of them
    aunt_money = (total_money - jade_money - julia_money) / 2

    # return the result
    result = aunt_money
    return result

print(solution())