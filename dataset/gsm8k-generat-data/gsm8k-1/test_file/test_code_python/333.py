def solution():
    """Luke ate 2 hot dogs. Thomas ate three times more hot dogs than Luke. John ate half the amount Thomas ate. How many more hot dogs did John eat than Luke?"""
    luke_hotdogs = 2
    thomas_hotdogs = luke_hotdogs * 3
    john_hotdogs = thomas_hotdogs / 2
    hotdogs_difference = john_hotdogs - luke_hotdogs
    result = hotdogs_difference
    return result

print(solution())