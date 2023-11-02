def solution():
    """There were 250 balloons in one package. Dante evenly shared the balloons among his 5 friends. Dante changed his mind and asked each of his friends to give him 11 balloons. How many balloons does each friend have now?"""
    # Calculate the initial number of balloons each friend received
    initial_balloons = 250 // 5

    # Calculate the number of balloons each friend has after giving 11 balloons back to Dante
    final_balloons = initial_balloons - 11

    # Display the final number of balloons each friend has
    result = final_balloons
    return result

print(solution())