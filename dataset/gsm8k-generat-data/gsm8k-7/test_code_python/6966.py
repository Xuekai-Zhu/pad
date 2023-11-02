def solution():
    text_cost = 1/30  # cost per text
    call_cost = 3/20  # cost per minute of call
    num_texts = 60
    num_minutes = 60
    monthly_cost = 12  # current plan cost

    # Calculate the cost of texts and calls on the alternative plan
    alt_cost = (num_texts * text_cost) + (num_minutes * call_cost)

    # Calculate the difference in cost between the current plan and the alternative plan
    savings = monthly_cost - alt_cost
    result = savings
    return result

print(solution())