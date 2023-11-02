def solution():
    katrina_money = 5  # Katrina earns $5.00 for signing up
    referral_money = 5  # Katrina earns $5.00 for each friend that signs up
    friends_signed_up = 5  # 5 friends signed up on the day Katrina signed up
    friends_signed_up_week = 7  # 7 more friends signed up during the week

    # Calculate the total money earned by Katrina and her friends
    total_money = katrina_money + referral_money * (friends_signed_up + friends_signed_up_week)
    result = total_money
    return result

print(solution())