def solution():
    """Shania is designing her own dress, and decides to make it a longer dress by extending the dress by 50% of its original length. She also adds 20cm to the bottom of the dress with a lace trim. If the final design is 140cm long then how long, in centimeters, was the dress in its original design?"""
    final_length = 140
    lace_trim = 20
    extended_percent = 50
    original_length = (final_length - lace_trim) / (1 + extended_percent / 100)
    result = original_length
    return result

print(solution())