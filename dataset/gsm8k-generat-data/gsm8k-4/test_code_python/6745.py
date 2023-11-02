def solution():
    """There were 250 balloons in one package. Dante evenly shared the balloons among his 5 friends. Dante changed his mind and asked each of his friends to give him 11 balloons. How many balloons does each friend have now?"""
    # Define the number of balloons in the package
    balloons = 250

    # Define the number of friends
    friends = 5

    # Calculate the initial share of balloons per friend
    initial_share = balloons / friends

    # Calculate the new number of balloons per friend after giving 11 balloons to Dante
    new_share = (balloons - 11) / friends

    result = new_share
    return result

print(solution())