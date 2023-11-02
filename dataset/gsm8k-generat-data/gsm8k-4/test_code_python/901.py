def solution():
    """Sandi had $600. She spent half of it at a farmer’s market. Gillian spent $150 more than three times Sandi's total. What is the total that Gillian spent at the farmer’s market?"""
    # Define Sandi's initial budget and amount spent at the farmer's market
    sandi_budget = 600
    sandi_spent = sandi_budget / 2

    # Calculate Gillian's spending
    gillian_spent = 3 * sandi_spent + 150

    # Calculate the amount Gillian spent at the farmer's market
    gillian_farmers_market = gillian_spent - sandi_spent

    # return the result
    result = gillian_farmers_market
    return result

print(solution())