def solution():
    num_people = 1000  # There are 1000 people in the city
    bottom_percentile = 0.2  # The bottom 20% of people receive the stimulus
    stimulus_amount = 2000  # The stimulus amount is $2000
    tax_return_ratio = 5  # The stimulus returns 5 times as much money to the government

    # Calculate how many people receive the stimulus
    num_stimulus_recipients = int(num_people * bottom_percentile)

    # Calculate the total cost of the stimulus
    total_cost = num_stimulus_recipients * stimulus_amount

    # Calculate the total tax return from the stimulus
    total_tax_return = total_cost * tax_return_ratio

    # Calculate the government profit from the project
    government_profit = total_tax_return - total_cost
    result = government_profit
    return result

print(solution())