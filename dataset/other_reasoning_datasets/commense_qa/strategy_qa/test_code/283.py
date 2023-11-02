def solution():
    smooth_jazz_instruments = ["saxophone", "guitar", "piano", "trumpet", "synthesizer", "electric bass", "drums"]
    james_cotton_instrument = "blues harmonica"
    if james_cotton_instrument not in smooth_jazz_instruments:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())