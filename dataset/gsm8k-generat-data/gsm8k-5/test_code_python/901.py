def solution():
    sandis_spending = 600 / 2  # Sandi spent half of her money at the farmer's market
    gillians_spending = (3 * sandis_spending) + 150  # Gillian spent $150 more than three times Sandi's spending

    # Calculate the total amount Gillian spent at the farmer's market
    gillians_farmers_market_spending = gillians_spending - (600 / 2)
    result = gillians_farmers_market_spending
    return result

print(solution())