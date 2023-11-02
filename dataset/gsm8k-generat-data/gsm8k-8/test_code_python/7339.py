def solution():
    # Calculate the total amount of milk Brooke has
    total_milk = 12 * 4

    # Calculate the total amount of milk sold
    milk_sold = 6 * 6

    # Calculate the amount of milk turned into butter
    milk_to_butter = total_milk - milk_sold

    # Calculate the amount of butter Brooke has
    butter = milk_to_butter * 2

    # Calculate the total amount of money earned from selling milk
    milk_money = milk_sold * 3

    # Calculate the total amount of money earned from selling butter
    butter_money = butter * 1.5

    # Calculate the total amount of money Brooke earns
    total_money = milk_money + butter_money
    result = total_money
    return result

print(solution())