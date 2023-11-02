def solution():
    money_received = 50  # Jesse received $50 as a gift
    cost_of_novel = 7  # The cost of the novel Jesse likes is $7
    cost_of_lunch = 2 * cost_of_novel  # Jesse spent twice as much on lunch as she did on the novel
    total_spent = cost_of_novel + cost_of_lunch  # Calculate the total amount Jesse spent

    # Calculate the amount of money Jesse has left after going to the mall
    money_left = money_received - total_spent
    result = money_left
    return result

print(solution())