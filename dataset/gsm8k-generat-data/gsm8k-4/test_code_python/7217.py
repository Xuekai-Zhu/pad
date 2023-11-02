def solution():
    """The mayor commissioned two artists to paint 50 murals around the city. Once the work was completed, Celina was paid $1,000 more than 4 times the amount Diego got. If the mayor paid the two a total of $50,000, how much did Diego get?"""
    # Define the total number of murals and the total payment
    TOTAL_MURALS = 50
    TOTAL_PAYMENT = 50000

    # Define the payment ratio of Celina to Diego
    CELINA_TO_DIEGO_RATIO = 4

    # Calculate the total payment received by Celina and Diego
    total_payment_cd = TOTAL_PAYMENT - 1000

    # Calculate the sum of Celina's and Diego's payment
    cd_payment_sum = (1 + CELINA_TO_DIEGO_RATIO) * total_payment_cd / (1 + CELINA_TO_DIEGO_RATIO + 1)

    # Calculate Diego's payment
    diego_payment = total_payment_cd - cd_payment_sum

    result = round(diego_payment)
    return result

print(solution())