def solution():
    connie_payback = 30000
    connie_share = 0.5

    # Calculate the total amount Connie got from selling the land
    total_land_sale = connie_payback / connie_share

    # Calculate the amount of money Connie used to buy the land
    initial_land_price = total_land_sale / 3

    # Calculate the initial amount of money Blake gave to Connie
    initial_money = initial_land_price + connie_payback
    result = initial_money
    return result

print(solution())