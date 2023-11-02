def solution():
    """John has taken 10 pictures every day for the past 3 years. He saves them in raw format so each memory card can store 50 images. Each memory card costs $60. How much does he spend on memory cards?"""
    # Define the number of pictures John takes every day and every year
    daily_pictures = 10
    yearly_pictures = daily_pictures * 365

    # Define the number of memory cards John needs every year and the total cost
    yearly_cards = yearly_pictures // 50 + 1
    yearly_cost = yearly_cards * 60

    # Calculate the total cost for 3 years
    total_cost = yearly_cost * 3

    # return the result
    result = total_cost
    return result

print(solution())