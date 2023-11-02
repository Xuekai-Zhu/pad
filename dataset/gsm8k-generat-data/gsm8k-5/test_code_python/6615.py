def solution():
    pete_money = 250  # Pete received $2.50, which is 250 cents
    raymond_money = 250  # Raymond also received $2.50
    pete_spent = 20  # 4 nickels at 5 cents each
    raymond_spent = raymond_money - (10 * 7)  # Raymond has 7 dimes left, so he spent 18 dimes (180 cents)

    # Calculate the total amount spent by Pete and Raymond
    total_spent = pete_spent + raymond_spent
    result = total_spent
    return result

print(solution())