def solution():
    # Define the amount of strawberries picked by Christine
    chris_strawberries = 10

    # Define the amount of strawberries picked by Rachel
    rachel_strawberries = chris_strawberries * 2

    # Calculate the total amount of strawberries
    total_strawberries = chris_strawberries + rachel_strawberries

    # Calculate the number of pies they can make
    pies = total_strawberries // 3

    result = pies
    return result

print(solution())