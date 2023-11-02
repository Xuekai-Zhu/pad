def solution():
    # Calculate the number of capsules of 100 mg amoxicillin sold
    revenue_100 = 80  # Heisenberg earned $80 from 100 mg amoxicillin every week
    cost_100 = 5  # Each capsule of 100 mg amoxicillin costs $5
    quantity_100 = revenue_100 / cost_100  # Calculate the number of capsules sold

    # Calculate the number of capsules of 500 mg amoxicillin sold
    revenue_500 = 60  # Heisenberg earned $60 from 500 mg amoxicillin every week
    cost_500 = 2  # Each capsule of 500 mg amoxicillin costs $2
    quantity_500 = revenue_500 / cost_500  # Calculate the number of capsules sold

    # Calculate the total number of capsules sold in 2 weeks
    total_quantity = (quantity_100 + quantity_500) * 2

    result = total_quantity
    return result

print(solution())