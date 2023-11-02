def solution():
    # Define the total amount of sand initially covering the treasure
    initial_sand = 8

    # Calculate the amount of sand after the tropical storm
    storm_sand = initial_sand / 2

    # Calculate the total amount of sand after the tsunami wave
    total_sand = storm_sand + 2

    # Calculate the amount of sand Pirate Rick had to dig up to reach the treasure
    sand_to_dig = initial_sand - storm_sand

    # Calculate the time it took for Pirate Rick to dig up the treasure
    time_to_dig = sand_to_dig / 8

    result = time_to_dig
    return result

print(solution())