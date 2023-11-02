def solution():
    communism_belief = "no private ownership of property"
    trickle_down_economics = "rich businesses getting tax breaks to pass wealth to the poor"
    if communism_belief not in trickle_down_economics:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())