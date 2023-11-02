def solution():
    """Mr. Alonzo harvested 245.5 kg of tomatoes. He sold 125.5 kg to Mrs. Maxwell and 78 kg to Mr. Wilson. How many kilograms of tomatoes are not sold?"""
    # Define the total amount of tomatoes harvested
    total_tomatoes = 245.5

    # Calculate the amount of tomatoes sold to Mrs. Maxwell and Mr. Wilson
    sold_tomatoes = 125.5 + 78

    # Calculate the amount of tomatoes not sold
    unsold_tomatoes = total_tomatoes - sold_tomatoes

    # Return the result
    result = unsold_tomatoes
    return result

print(solution())