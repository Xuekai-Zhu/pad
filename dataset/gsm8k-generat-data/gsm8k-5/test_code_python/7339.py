def solution():
    cows = 12  # Brooke has 12 cows
    milk_per_cow = 4  # Each cow produces 4 gallons of milk
    total_milk = cows * milk_per_cow  # Total milk produced by all cows
    milk_sell = 6 * 6  # Brooke's 6 customers each want 6 gallons of milk

    # Calculate the milk that Brooke has left to turn into butter
    milk_butter = total_milk - milk_sell

    # Calculate the butter inventory and price
    butter_sticks = milk_butter * 2  # One gallon of milk equals 2 sticks of butter
    butter_price = butter_sticks * 1.5  # Brooke sells each stick of butter for $1.5

    # Calculate the milk's revenue and butter's revenue
    milk_revenue = milk_sell * 3  # Brooke sells each gallon of milk for $3
    butter_revenue = butter_price

    # Calculate the total revenue 
    total_revenue = milk_revenue + butter_revenue
    result = total_revenue
    return result

print(solution())