def solution():
    """The Smith family is getting ready for summer and needs to have their swimming pool filled. The pool company instructed them to measure to find the volume of the pool, then to multiply it by 5.9 to calculate how many gallons of water they need. The cost for the pool company to come and fill the pool is $0.10 per gallon. Mr. Smith measured and found the pool is 14 feet wide, 25 feet long, and 4 feet deep. How much will it cost to fill the pool?"""
    width = 14
    length = 25
    depth = 4
    volume = width * length * depth
    gallons = volume * 5.9
    cost = gallons * 0.10
    result = cost
    return result

print(solution())