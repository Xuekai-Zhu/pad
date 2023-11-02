def solution():
    """Artie has a flower stand at the Farmers Market. He sells three kinds of flowers: marigolds, petunias, and begonias.
    He usually sells marigolds for $2.74 per pot, petunias for $1.87 per pot, and begonias for $2.12 per pot.
    Artie has no change today, so he has decided to round all his prices to the nearest dollar.
    If Artie sells 12 pots of marigolds, 9 pots of petunias, and 17 pots of begonias, how much will he make?"""
    marigolds_price = round(2.74)
    petunias_price = round(1.87)
    begonias_price = round(2.12)
    marigolds_sold = 12
    petunias_sold = 9
    begonias_sold = 17
    total_sales = (marigolds_price * marigolds_sold) + (petunias_price * petunias_sold) + (begonias_price * begonias_sold)
    result = total_sales
    return result

print(solution())