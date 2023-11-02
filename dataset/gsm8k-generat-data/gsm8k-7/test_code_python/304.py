def solution():
    # Define the number of acres each farmer has
    bob_corn = 3
    bob_cotton = 9
    bob_beans = 12

    brenda_corn = 6
    brenda_cotton = 7
    brenda_beans = 14

    bernie_corn = 2
    bernie_cotton = 12

    # Define the water requirements for each crop
    corn_water = 20
    cotton_water = 80
    beans_water = corn_water * 2

    # Calculate the total water used for each farmer
    bob_water = (bob_corn * corn_water) + (bob_cotton * cotton_water) + (bob_beans * beans_water)
    brenda_water = (brenda_corn * corn_water) + (brenda_cotton * cotton_water) + (brenda_beans * beans_water)
    bernie_water = (bernie_corn * corn_water) + (bernie_cotton * cotton_water)

    # Calculate the total water used
    total_water = bob_water + brenda_water + bernie_water

    # Calculate the percentage of the total water used that goes to Bob's farm
    bob_percentage = (bob_water / total_water) * 100

    result = bob_percentage
    return result

print(solution())