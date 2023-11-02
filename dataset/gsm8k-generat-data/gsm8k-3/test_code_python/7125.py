def solution():
    """Tomorrow, Pete must finish paying off the last $90 he owes on a bike. He goes through his wallet and finds two $20 bills. Checking his pockets, he finds four $10 bills. Unhappy that he doesn't have the entire amount, he suddenly remembers that he has plastic bottles that can be returned to his local store for cash. If the store pays 50 cents for each bottle, how many bottles will Pete have to return to the store?"""
    # Define the amount of money Pete already has
    money = 2 * 20 + 4 * 10

    # Calculate the remaining amount he needs
    remaining = 90 - money

    # Calculate the number of bottles he needs to return
    bottles = remaining / 0.5

    # Round up to the nearest whole number of bottles
    bottles = math.ceil(bottles)

    # Display the number of bottles he needs to return
    result = bottles
    return result

print(solution())