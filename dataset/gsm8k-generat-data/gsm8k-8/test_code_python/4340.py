def solution():
    # Define the number of kids attending each class
    saturday_kids = 20
    sunday_kids = saturday_kids / 2

    # Calculate the total money made from both classes
    saturday_money = saturday_kids * 10
    sunday_money = sunday_kids * 10
    total_money = saturday_money + sunday_money

    result = total_money
    return result

print(solution())