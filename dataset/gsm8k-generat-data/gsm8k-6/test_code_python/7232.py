def solution():
    initial_savings = 230  # initial savings in Emma's bank account
    shoe_cost = 60  # cost of shoes Emma bought
    deposited = 2 * shoe_cost  # amount deposited the next week
    current_savings = initial_savings - shoe_cost + deposited  # calculate current savings
    result = current_savings
    return result

print(solution())