def solution():
    """Michael wants to dig a hole 400 feet less deep than twice the depth of the hole that his father dug. 
    The father dug a hole at a rate of 4 feet per hour. If the father took 400 hours to dig his hole, 
    how many hours will it take for Michael to dig a hole that is 400 feet less than twice as deep as his father's hole working at the same rate?"""
    # Calculate the depth of the father's hole
    father_depth = 4 * 400

    # Calculate the depth of Michael's hole
    michael_depth = (2 * father_depth) - 400

    # Calculate the number of hours Michael will need to dig his hole
    michael_hours = michael_depth / 4

    result = michael_hours
    return result

print(solution())