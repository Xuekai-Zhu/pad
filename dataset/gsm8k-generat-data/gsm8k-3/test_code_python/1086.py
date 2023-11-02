def solution():
    """Mr. Alonzo harvested 245.5 kg of tomatoes. He sold 125.5 kg to Mrs. Maxwell and 78 kg to Mr. Wilson. How many kilograms of tomatoes are not sold?"""
    # Define the amount of tomatoes harvested and sold
    harvested = 245.5
    sold_to_maxwell = 125.5
    sold_to_wilson = 78

    # Calculate the amount of tomatoes not sold
    not_sold = harvested - sold_to_maxwell - sold_to_wilson

    # Display the amount of tomatoes not sold
    result = not_sold
    return result

print(solution())