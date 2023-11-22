def solution():
    
    # Define the initial value of the sapphires and rubies
    initial_sapphire_value = 800
    initial_rubie_value = 1200

    # Calculate the value of the traded 2 sapphires and the remaining rubies
    traded_sapphire_value = 3 * initial_sapphire_value
    remaining_rubie_value = 2 * initial_rubie_value

    # Calculate the total value of the jewels
    total_value = traded_sapphire_value + remaining_rubie_value

    # return the result
    result = total_value
    return result

print(solution())