def solution():
    inheritance = 124600
    shelby_share = inheritance / 2
    remaining_share = inheritance - shelby_share
    num_grandchildren = 10

    # Calculate the share of each of the remaining grandchildren
    per_grandchild_share = remaining_share / num_grandchildren

    result = per_grandchild_share
    return result

print(solution())