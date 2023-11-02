def solution():
    catholic_beliefs = ["one-to-one match between man and woman"]
    forbidden_actions = ["coveting your neighbor's wife"]
    if "polyamory" not in catholic_beliefs and "polyamory" not in forbidden_actions:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())