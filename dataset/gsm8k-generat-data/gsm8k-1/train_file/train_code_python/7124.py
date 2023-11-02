def solution():
    """Tomorrow, Pete must finish paying off the last $90 he owes on a bike. He goes through his wallet and finds two $20 bills. Checking his pockets, he finds four $10 bills. Unhappy that he doesn't have the entire amount, he suddenly remembers that he has plastic bottles that can be returned to his local store for cash. If the store pays 50 cents for each bottle, how many bottles will Pete have to return to the store?"""
    remaining_balance = 90
    cash_in_wallet = (2 * 20) + (4 * 10)
    cash_needed = remaining_balance - cash_in_wallet
    bottles_needed = cash_needed / 0.5
    result = bottles_needed
    return result

print(solution())