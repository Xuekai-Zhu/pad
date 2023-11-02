def solution():
     """Colby harvested his mango trees, the total mangoes he harvested is 60 kilograms. He sold 20 kilograms to the market and sold the remaining half to his community. If each kilogram contains 8 mangoes, how many mangoes does he still have?"""
     mangoes_harvested = 60
     mangoes_sold = 20
     mangoes_left = mangoes_harvested - mangoes_sold
     mangoes_community = mangoes_left / 2
     mangoes_remaining = mangoes_left - mangoes_community
     mangoes_per_kilogram = 8
     result = mangoes_remaining * mangoes_per_kilogram
     return result

print(solution())