def solution():
    """Brooke is milking cows and then selling the milk at the market for $3 a gallon. Whatever milk doesn't sell, she turns into butter. One gallon of milk equals 2 sticks of butter. She then sells the butter for $1.5 a stick. She has 12 cows. Each cow produces 4 gallons of milk. She has 6 customers, each of whom wants 6 gallons of milk. How much money does she earn if she sells all her milk and butter?"""
    # Define the prices of milk and butter
    MILK_PRICE = 3
    BUTTER_PRICE = 1.5

    # Calculate the total amount of milk produced by all the cows
    total_milk = 12 * 4

    # Determine how much milk to sell and how much to turn into butter
    milk_to_sell = 6 * 6
    milk_to_turn_into_butter = total_milk - milk_to_sell

    # Calculate the total amount of butter produced
    total_butter = milk_to_turn_into_butter * 2

    # Calculate the total earnings from selling milk
    milk_earnings = milk_to_sell * MILK_PRICE

    # Calculate the total earnings from selling butter
    butter_earnings = total_butter * BUTTER_PRICE

    # Calculate the total earnings
    total_earnings = milk_earnings + butter_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())