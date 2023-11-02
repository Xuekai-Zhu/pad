def solution():
    bitcoin_price_in_2017 = 19783
    volkswagen_jetta_price = 18895
    # Divide bitcoin price by Volkswagen Jetta price to check how many Jettas one bitcoin could cover
    if bitcoin_price_in_2017 >= volkswagen_jetta_price:
        jettas_per_bitcoin = bitcoin_price_in_2017 / volkswagen_jetta_price
        result = f"Yes, one bitcoin in 2017 could cover {jettas_per_bitcoin} Volkswagen Jettas"
    else:
        result = "No, one bitcoin in 2017 could not cover the cost of a Volkswagen Jetta"
    return result

print(solution())