def solution():
    """Michael wants to dig a hole 400 feet less deep than twice the depth of the hole that his father dug. The father dug a hole at a rate of 4 feet per hour. If the father took 400 hours to dig his hole, how many hours will it take for Michael to dig a hole that is 400 feet less than twice as deep as his father's hole working at the same rate?"""
    # Define the rate of digging for both Michael and his father in feet per hour
    rate = 4

    # Define the depth of the father's hole in feet and the time it took to dig it in hours
    father_depth = rate * 400
    father_time = 400

    # Calculate the depth of Michael's hole and the time it will take to dig it in hours
    michael_depth = 2 * father_depth - 400
    michael_time = michael_depth / rate

    # Display the time it will take Michael to dig his hole
    result = michael_time
    return result

print(solution())