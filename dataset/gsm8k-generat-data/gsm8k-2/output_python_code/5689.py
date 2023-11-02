def solution():
    """Fred has 12 identical candy bars, and Uncle Bob has 6 more. If Jacqueline has ten times the total number of candy bars Fred and Uncle Bob have, what's 40% of Jacqueline's candy bars?"""
    fred_candy = 12
    uncle_bob_candy = fred_candy + 6
    total_candy = fred_candy + uncle_bob_candy
    jacqueline_candy = 10 * total_candy
    forty_percent = 0.4 * jacqueline_candy
    result = forty_percent
    return result

print(solution())