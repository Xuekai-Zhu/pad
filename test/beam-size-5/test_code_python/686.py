def solution():
    
    # Define the number of coins saved by Rong per month
    rong_coins = 20

    # Define the number of coins saved by Neil per month
    neil_coins = (2/5) * rong_coins

    # Calculate the total number of coins saved by Rong in 10 years
    rong_total = rong_coins * 12 * 10

    # Calculate the total number of coins saved by Neil in 10 years
    neil_total = neil_coins * 12 * 10

    # Calculate the total number of coins saved by both of them
    total_coins = rong_total + neil_total

    # Display the total number of coins saved
    result = total_coins
    return result

print(solution())