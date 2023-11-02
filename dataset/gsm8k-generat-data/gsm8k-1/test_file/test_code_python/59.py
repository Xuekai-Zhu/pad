def solution():
    """Aleena subscribed to a streaming service that charges her $140 per month. If the streaming company charged her the initial amount for the first half of the year and then charged her 10% less money on the other half of the year, calculate the total amount she had paid for the streaming service by the end of the year."""
    monthly_cost = 140
    first_half = 6
    second_half = 6
    initial_payment = monthly_cost * first_half
    reduced_cost = monthly_cost * 0.9
    reduced_payment = reduced_cost * second_half
    total_payment = initial_payment + reduced_payment
    result = total_payment
    return result

print(solution())