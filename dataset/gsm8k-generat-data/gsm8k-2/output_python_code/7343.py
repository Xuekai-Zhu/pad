def solution():
    """The cheerleading coach is ordering new uniforms. There are 4 cheerleaders who need a size 2, a certain number who need a size 6, and half that number who need a size 12. If there are 19 cheerleaders total, how many cheerleaders need a size 6?"""
    total_cheerleaders = 19
    size_2_cheerleaders = 4
    size_12_cheerleaders = total_cheerleaders - size_2_cheerleaders
    size_6_cheerleaders = (size_12_cheerleaders / 2) - (size_2_cheerleaders / 2)
    result = size_6_cheerleaders
    return result

print(solution())