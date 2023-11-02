def solution():
    # Define the amount of ground beef purchased
    total_beef = 4 * 5

    # Calculate the number of burgers that can be made
    burgers = total_beef // 2
    
    # Calculate the number of people that can be invited
    guests = burgers + 1
    
    result = guests
    return result

print(solution())