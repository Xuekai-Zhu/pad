def solution():
    required_instruments = ["trumpet", "timpani", "oboe", "violin", "viola"]
    bruce_gandy_instrument = "bagpipe"
    if bruce_gandy_instrument not in required_instruments:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())