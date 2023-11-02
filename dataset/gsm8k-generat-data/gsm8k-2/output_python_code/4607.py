def solution():
    """Juanita enters a drumming contest. It costs $10 to enter. She has 2 minutes to hit as many drums as she can. If she hits 200 drums, she can start to make money, equal to 2.5 cents for every drum hit. How many drums does she hit if she lost $7.5 for joining the contest?"""
    contest_fee = 10
    drum_hits_for_profit = 200
    profit_per_drum_hit = 0.025
    lost_money = 7.5

    total_profit = (drum_hits_for_profit * profit_per_drum_hit) - contest_fee - lost_money
    drums_hit = total_profit / profit_per_drum_hit

    result = drums_hit
    return result

print(solution())