def solution():
    """Celina enjoys hiking in the mountains. Due to a lack of proper equipment, she decided to order a new pair of boots, a flashlight, and a special hoodie. The hoodie cost $80 and the flashlight was only 20% of that price. The pair of boots cost was $110, but due to a special promotion, Celina was able to buy them 10% cheaper. How much did Celina spend in total on the above-mentioned equipment?"""
    # Define the price of the hoodie
    hoodie_price = 80

    # Calculate the price of the flashlight
    flashlight_price = hoodie_price * 0.2

    # Define the original price of the boots
    boots_price = 110

    # Calculate the discounted price of the boots
    boots_discount = boots_price * 0.1
    boots_final_price = boots_price - boots_discount

    # Calculate the total cost of all the equipment
    total_cost = hoodie_price + flashlight_price + boots_final_price

    # Display the total cost
    result = total_cost
    return result

print(solution())