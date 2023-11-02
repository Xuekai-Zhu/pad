def solution():
    """Regina has a farm with animals. She has 20 cows and four times more pigs. Someone told her, that she could sell all the animals and earn $400 for each pig and $800 for each cow. How much money would she earn if she would sell all the animals from the farm?"""
    # Define the number of cows and pigs on Regina's farm
    cows = 20
    pigs = 4 * cows

    # Calculate the total amount of money Regina could earn by selling all the animals
    total_money = (cows * 800) + (pigs * 400)

    # Display the total amount of money Regina could earn
    result = total_money
    return result

print(solution())