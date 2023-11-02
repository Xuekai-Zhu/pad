def solution():
    leafhoppers_feed_on_sap = True
    maple_syrup_contains_sap = True
    if leafhoppers_feed_on_sap and maple_syrup_contains_sap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())