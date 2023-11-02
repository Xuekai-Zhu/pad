def solution():
    num_barry = 24
    barry_nice = num_barry

    num_kevin = 20
    kevin_nice = num_kevin / 2

    num_julie = 80
    julie_nice = num_julie * 0.75

    num_joe = 50
    joe_nice = num_joe * 0.1

    # Calculate the total number of nice people in the crowd
    total_nice = barry_nice + kevin_nice + julie_nice + joe_nice
    result = total_nice
    return result

print(solution())