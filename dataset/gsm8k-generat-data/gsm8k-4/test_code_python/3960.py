def solution():
    """Voltaire and Leila are vloggers, Voltaire has an average of 50 viewers per day while Leila has twice the number of viewers Voltaire has. If they earn $0.50 per view, how much does Leila earn per week?"""
    # Define Voltaire's average viewers per day
    voltaire_viewers = 50

    # Define Leila's average viewers per day
    leila_viewers = voltaire_viewers * 2

    # Calculate the total number of viewers in a week
    total_viewers = (voltaire_viewers + leila_viewers)*7

    # Calculate Leila's earnings per week
    leila_earnings = total_viewers * 0.5

    # Return the result
    result = leila_earnings
    return result

print(solution())