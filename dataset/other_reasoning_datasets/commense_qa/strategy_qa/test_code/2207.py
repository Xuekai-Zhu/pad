def solution():
    march_named_after = "Mars"
    jupiter = "Jupiter"
    junon = "Juno"
    mars_parents = [jupiter, junon]
    if march_named_after == "Mars" and jupiter in mars_parents:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())