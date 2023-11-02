def solution():
    """Tomorrow, Pete must finish paying off the last $90 he owes on a bike. He goes through his wallet and finds two $20 bills. Checking his pockets, he finds four $10 bills. Unhappy that he doesn't have the entire amount, he suddenly remembers that he has plastic bottles that can be returned to his local store for cash. If the store pays 50 cents for each bottle, how many bottles will Pete have to return to the store?"""
    # Define the total amount of money Pete has
    total_money = (2*20) + (4*10)

    # Calculate how much money he still needs to pay for the bike
    remaining_money = 90 - total_money

    # Calculate how many bottles he needs to return to the store
    bottles = remaining_money / 0.5

    # Return the number of bottles as an integer
    result = int(bottles)
    return result

print(solution())