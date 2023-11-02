def solution():
    """Jerry, Gabriel, and Jaxon ask their parents to buy them toys to play with.Jerry is bought 8 more toys than Gabriel but Gabriel has twice as many toys as Jaxon. If Jaxon got 15 toys, what's the total number of toys they all have?"""
    jaxon_toys = 15
    gabriel_toys = jaxon_toys * 2
    jerry_toys = gabriel_toys + 8
    total_toys = jaxon_toys + gabriel_toys + jerry_toys
    result = total_toys
    return result

print(solution())