def solution():
    """John has taken 10 pictures every day for the past 3 years.  He saves them in raw format so each memory card can store 50 images.  Each memory card costs $60.  How much does he spend on memory cards?"""
    # Define the number of pictures taken in a day and the number of years
    PICTURES_PER_DAY = 10
    NUM_YEARS = 3

    # Calculate the total number of pictures taken
    total_pictures = PICTURES_PER_DAY * 365 * NUM_YEARS

    # Calculate the number of memory cards needed
    num_cards = (total_pictures // 50) + 1

    # Calculate the total cost of the memory cards
    total_cost = num_cards * 60

    # Display the total cost
    result = total_cost
    return result

print(solution())