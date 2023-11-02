def solution():
    
    # Define the initial number of sapphires and rubies
    initial_sapphires = 8
    initial_rubies = 2

    # Define the value of each type of jenna's jewel
    sapphire_value = 800
    rubie_value = 1200

    # Calculate the value of the traded sapphires
    traded_sapphires_value = 3 * sapphire_value

    # Calculate the value of the rubies
    rubie_value = 2 * rubie_value

    # Calculate the total value of all the jewels
    total_value = initial_sapphires_value + rubie_value

    # return the result
    result = total_value
    return result

print(solution())