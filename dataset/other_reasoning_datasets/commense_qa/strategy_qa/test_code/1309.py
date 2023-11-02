def solution():
    peta_blacklist = ["unacceptable", "should be avoided", "excluded"]
    michael_vick = "vicious dog fighting enterprise"
    if any(word in michael_vick for word in peta_blacklist):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())