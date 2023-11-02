def solution():
    """During 5 hours, a spider can catch 9 flies. How many flies would this spider catch in 30 hours if he would keep his efficiency?"""
    # Define the spider's efficiency in flies per hour
    efficiency = 9 / 5

    # Calculate the number of flies the spider would catch in 30 hours
    flies_catched = efficiency * 30

    # Display the number of flies the spider would catch
    result = flies_catched
    return result

print(solution())