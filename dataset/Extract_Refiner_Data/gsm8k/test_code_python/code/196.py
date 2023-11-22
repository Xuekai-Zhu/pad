def solution():
    
    # Define the number of pails of water Baldur gets every morning and afternoon
    morning_pails = 5
    afternoon_pails = 6

    # Define the number of liters of water in each pail
    liters_per_pail = 5

    # Calculate the total number of pails of water Baldur gets every day
    total_pails = morning_pails + afternoon_pails
    total_liters = total_pails * liters_per_pail

    # Display the total number of liters of water Baldur gets every day
    result = total_liters
    return result

print(solution())