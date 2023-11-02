def solution():
    initial_money = 30  # Lizzy had $30
    loaned_money = 15  # Lizzy loaned out $15 to her friend
    friend_returned_money = loaned_money * 1.2  # Lizzy's friend returned the money with a 20% interest
    final_money = initial_money - loaned_money + friend_returned_money  # Calculate Lizzy's final money
    result = final_money
    return result

print(solution())