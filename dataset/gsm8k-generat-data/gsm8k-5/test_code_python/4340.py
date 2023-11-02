def solution():
    # Saturday's class
    saturday_kids = 20
    saturday_money = saturday_kids * 10

    # Sunday's class
    sunday_kids = saturday_kids / 2  # Half as many as Saturday
    sunday_money = sunday_kids * 10

    # Total money made
    total_money = saturday_money + sunday_money
    result = total_money
    return result

print(solution())