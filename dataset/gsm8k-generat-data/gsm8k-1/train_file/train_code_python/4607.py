def solution():
    """Juanita enters a drumming contest. It costs $10 to enter. She has 2 minutes to hit as many drums as she can. If she hits 200 drums, she can start to make money, equal to 2.5 cents for every drum hit. How many drums does she hit if she lost $7.5 for joining the contest?"""
    entry_fee = 10
    money_lost = 7.5
    total_money_lost = entry_fee + money_lost
    drum_hits_needed = 200
    money_per_drum_hit = 0.025
    total_money_made = total_money_lost / money_per_drum_hit
    drums_hit = (total_money_made - drum_hits_needed) / 2.5
    result = drums_hit
    return result

print(solution())