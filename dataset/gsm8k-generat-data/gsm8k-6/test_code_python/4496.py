def solution():
    # Calculate the amount of tuition remaining after deducting the saved amount
    remaining_tuition = 30000 - 10000  # the total tuition cost is $30,000 and Sabina already saved $10,000
    grant_amount = 0.4 * remaining_tuition  # the grant will cover 40% of the remaining tuition

    # Calculate the total amount of loan needed to cover the tuition
    loan_amount = remaining_tuition - grant_amount
    result = loan_amount
    return result

print(solution())