def solution():
    
    inheritance = 124600
    shelby_share = inheritance / 2
    remaining_share = inheritance - shelby_share
    grandchildren_count = 10
    each_grandchild_share = remaining_share / grandchildren_count
    result = each_grandchild_share
    return result

print(solution())