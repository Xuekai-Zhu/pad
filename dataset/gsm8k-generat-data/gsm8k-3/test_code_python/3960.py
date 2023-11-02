def solution():
    """Voltaire and Leila are vloggers, Voltaire has an average of 50 viewers per day while Leila has twice the number of viewers Voltaire has. If they earn $0.50 per view, how much does Leila earn per week?"""
    # Define Voltaire's average viewers per day and Leila's as twice the amount
    voltaire_viewers = 50
    leila_viewers = voltaire_viewers * 2

    # Calculate the total viewers for the week for each vlogger
    voltaire_weekly_viewers = voltaire_viewers * 7
    leila_weekly_viewers = leila_viewers * 7

    # Calculate the earnings for each vlogger
    voltaire_earnings = voltaire_weekly_viewers * 0.5
    leila_earnings = leila_weekly_viewers * 0.5

    # Display Leila's earnings for the week
    result = leila_earnings
    return result

print(solution())