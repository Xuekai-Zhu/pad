def solution():
    """Ursula is working at a marketing firm. She created a 30-second long commercial. Her boss told her that this commercial is too long to air and told her to shorten the commercial by 30%. How long will this commercial be after Ursula makes the desired changes?"""
    original_length = 30 # seconds
    reduction_percent = 30
    reduction_amount = original_length * (reduction_percent / 100)
    new_length = original_length - reduction_amount
    result = new_length
    return result

print(solution())