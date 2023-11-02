def solution():
    # Calculate the total number of coins put in during the first 4 hours
    total_coins = 20 + 30*2 + 40  # in the first hour 20 coins were put then in the next two hours 30 coins each time, and in the fourth hour 40 coins were put

    # Subtract the 20 coins taken out in the fifth hour
    remaining_coins = total_coins - 20 

    result = remaining_coins
    return result

print(solution())