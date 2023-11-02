def solution():
    """Sandi had $600. She spent half of it at a farmer’s market. Gillian spent $150 more than three times Sandi's total. What is the total that Gillian spent at the farmer’s market?"""
    # Calculate how much Sandi spent at the farmer's market
    sandi_spent = 600 / 2

    # Calculate how much Gillian spent in total
    gillian_total = 3 * sandi_spent + 150

    # Calculate how much Gillian spent at the farmer's market
    gillian_farmer_market = gillian_total - (600 - sandi_spent)

    # Display how much Gillian spent at the farmer's market
    result = gillian_farmer_market
    return result

print(solution())