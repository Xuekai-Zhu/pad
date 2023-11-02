def solution():
    daragh_bears = 20  # total number of bears Daragh had
    favorite_bears = 8  # number of favorite bears Daragh took out
    remaining_bears = daragh_bears - favorite_bears  # number of bears left after taking out favorites
    eden_bears = 10  # number of bears Eden had before division
    other_sisters_bears = remaining_bears // 3  # number of bears each of the other sisters got
    eden_bears_now = eden_bears + other_sisters_bears  # total number of bears Eden has now
    result = eden_bears_now
    return result

print(solution())