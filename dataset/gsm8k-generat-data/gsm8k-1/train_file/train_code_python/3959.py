def solution():
    """Voltaire and Leila are vloggers, Voltaire has an average of 50 viewers per day while Leila has twice the number of viewers Voltaire has. If they earn $0.50 per view, how much does Leila earn per week?"""
    
    voltaire_views_per_day = 50
    leila_views_per_day = voltaire_views_per_day * 2
    
    views_per_week = (voltaire_views_per_day + leila_views_per_day) * 7
    earnings_per_view = 0.50
    leila_earnings_per_week = leila_views_per_day * earnings_per_view * 7
    
    result = leila_earnings_per_week
    return result

print(solution())