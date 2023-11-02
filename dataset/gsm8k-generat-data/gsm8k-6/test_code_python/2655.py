def solution():
    sticky_strips = 15  # number of decorations hung with sticky strips
    rest_decorations = 1 - (2/3)  # fraction of decorations that are not hung with nails
    thumbtack_decorations = (2/5) * rest_decorations  # fraction of rest_decorations that are hung with thumbtacks
    nail_decorations = rest_decorations - thumbtack_decorations  # fraction of rest_decorations that are hung with nails
    total_nails = nail_decorations * (2/3)  # number of decorations hung with nails
    result = total_nails
    return result

print(solution())