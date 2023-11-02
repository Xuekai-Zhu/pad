def solution():
    wife_savings_per_week = 100  # The wife saves $100 every week
    husband_savings_per_month = 225  # The husband saves $225 every month
    total_savings = (wife_savings_per_week * 4 * 4) + (husband_savings_per_month * 4)  # After 4 months of savings
    investments = total_savings / 2  # They decide to invest half of their money
    shares = investments / 50  # Each share of stocks costs $50

    result = shares
    return result

print(solution())