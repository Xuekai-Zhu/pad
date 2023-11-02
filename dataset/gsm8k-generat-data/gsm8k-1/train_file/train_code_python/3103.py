def solution():
    """Mark wants to tip his server 20% on a $200 check. If his friend agrees to kick in $10, how much should Mark add?"""
    check_amount = 200
    tip_percent = 20
    tip_amount = check_amount * (tip_percent / 100)
    total_amount = check_amount + tip_amount + 10
    mark_adds = tip_amount + 10
    result = mark_adds
    return result

print(solution())