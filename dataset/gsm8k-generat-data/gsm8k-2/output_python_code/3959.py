def solution():
    """Voltaire and Leila are vloggers, Voltaire has an average of 50 viewers per day while Leila has twice the number of viewers Voltaire has. If they earn $0.50 per view, how much does Leila earn per week?"""
    voltaire_viewers = 50
    leila_viewers = voltaire_viewers * 2
    daily_earnings = (voltaire_viewers + leila_viewers) * 0.5
    weekly_earnings = daily_earnings * 7
    result = weekly_earnings
    return result

print(solution())