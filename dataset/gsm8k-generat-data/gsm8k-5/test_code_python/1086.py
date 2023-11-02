def solution():
    total_harvested = 245.5  # Mr. Alonzo harvested 245.5 kg of tomatoes
    sold_to_maxwell = 125.5  # Mr. Alonzo sold 125.5 kg of tomatoes to Mrs. Maxwell
    sold_to_wilson = 78  # Mr. Alonzo sold 78 kg of tomatoes to Mr. Wilson

    # Calculate the total amount sold
    total_sold = sold_to_maxwell + sold_to_wilson

    # Calculate the amount not sold
    not_sold = total_harvested - total_sold
    result = not_sold
    return result

print(solution())