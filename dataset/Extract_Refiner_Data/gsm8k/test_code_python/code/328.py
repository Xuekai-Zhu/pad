def solution():
    
    # Define the total number of castles
    total_castles = 220

    # Calculate the number of ruins
    ruins = total_castles * 0.4

    # Calculate the number of unmanned ruined castles
    unmanned_ruined = ruins * 0.5

    # Display the number of unmanned ruined castles
    result = unmanned_ruined
    return result

print(solution())