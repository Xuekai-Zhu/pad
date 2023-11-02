def solution():
    # Define the initial number of passengers
    initial_passengers = 124

    # Calculate the number of passengers after the first layover
    layover1_passengers = initial_passengers - 58 + 24

    # Calculate the number of passengers after the second layover
    layover2_passengers = layover1_passengers - 47 + 14

    # Calculate the total number of passengers, including crew members
    total_passengers = layover2_passengers + 10

    result = total_passengers
    return result

print(solution())