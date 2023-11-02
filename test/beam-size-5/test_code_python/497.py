def solution():
    
    # Define the ratio of yards used by Mariah and her grandma
    mariah_to_grandma_ratio = 1/4
    grandma_to_yards_ratio = 1/2

    # Define the number of yards in a skein of yarn
    yards_in_skein = 364

    # Calculate the total number of yards used by Mariah and her grandma
    mariah_yards = yards_in_skein * mariah_to_grandma_ratio
    grandma_yards = yards_in_skein * grandma_to_grandma_ratio

    # Calculate the total number of yards used
    total_yards = mariah_yards + grandma_yards

    # Display the total number of yards used
    result = total_yards
    return result

print(solution())