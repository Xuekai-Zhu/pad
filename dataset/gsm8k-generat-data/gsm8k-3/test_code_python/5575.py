def solution():
    """Jade had $38 and her sister Julia had half as much money she had. On New Year's eve, their aunt gave each of them an equal amount of money so that they had a total of $97. How much did their aunt give each of them?"""
    # Define the initial amount of money Jade had
    jade_money = 38

    # Calculate Julia's initial amount of money
    julia_money = jade_money / 2

    # Calculate the total initial amount of money
    total_money = jade_money + julia_money

    # Calculate the amount of money each of them received from their aunt
    aunt_money = (97 - total_money) / 2

    # Display the amount of money each of them received
    result = aunt_money
    return result

print(solution())