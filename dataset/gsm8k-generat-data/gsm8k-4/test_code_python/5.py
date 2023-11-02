def solution():
    """Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?"""
    # Define the number of yellow plants
    yellow_plants = 10

    # Calculate the number of purple plants as 80% more than yellow plants
    purple_plants = yellow_plants * 1.8

    # Calculate the total number of yellow and purple plants
    total_yp_plants = yellow_plants + purple_plants

    # Calculate the number of green plants as 25% of the total number of yellow and purple plants
    green_plants = total_yp_plants * 0.25

    # Calculate the total number of plants in the garden
    total_plants = yellow_plants + purple_plants + green_plants

    # Return the result
    result = total_plants
    return result

print(solution())