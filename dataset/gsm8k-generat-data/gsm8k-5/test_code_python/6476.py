def solution():
    # Calculate how much Geoff spent on sneakers on Monday
    monday_spend = 60 / 2  # $60 equally between 2 pairs of sneakers

    # Calculate how much Geoff will spend on sneakers on Tuesday
    tuesday_spend = monday_spend * 4  # 4 times as much as Monday

    # Calculate how much Geoff will spend on sneakers on Wednesday
    wednesday_spend = monday_spend * 5  # 5 times as much as Monday

    # Calculate the total amount Geoff will spend on sneakers over the three days
    total_spent = monday_spend + tuesday_spend + wednesday_spend
    result = total_spent
    return result

print(solution())