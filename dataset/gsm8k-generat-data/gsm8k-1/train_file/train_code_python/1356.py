def solution():
    """Lizzy's mother gave her 80 cents and her father gave her 40 cents for keeping to her promise.
    She went to her uncle's and spent 50 cents buying candy for her little cousin. Her uncle gave her another 70 cents.
    How many cents does she have now?"""
    starting_total = 80 + 40
    candy_cost = 50
    uncle_gift = 70
    final_total = starting_total - candy_cost + uncle_gift
    result = final_total
    return result

print(solution())