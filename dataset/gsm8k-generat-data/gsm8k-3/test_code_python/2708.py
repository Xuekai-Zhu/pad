def solution():
    """Ofelia joined a saving challenge wherein she has to save twice the amount she saved from the previous month. In January, she saved $10. How much is she going to save in May?"""
    # Define the initial amount saved and the number of months
    saved = 10
    months = 5

    # Calculate the amount saved in May
    for i in range(2, months + 1):
        saved *= 2
    
    # Display the amount saved in May
    result = saved
    return result

print(solution())