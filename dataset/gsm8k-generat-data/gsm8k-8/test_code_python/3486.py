def solution():
    # Randy's current money after Smith gave him $200
    randy_current_money = 2000
    randy_current_money += 1200

    # Calculate Randy's money before he gave Sally $1200
    randy_money_before_sally = randy_current_money + 1200

    # Calculate Randy's money before Smith gave him $200
    randy_money_before_smith = randy_money_before_sally - 200

    result = randy_money_before_smith
    return result

print(solution())