def solution():
    
    # Define the total number of castles
    total_castles = 220

    # Calculate the number of ruins
    ruins = total_castles * 0.4

    # Calculate the number of unmanned castles
    unmanned_castles = ruins * 0.5

    # Display the number of unmanned castles
    result = unmanned_castles
    return result

print(solution())