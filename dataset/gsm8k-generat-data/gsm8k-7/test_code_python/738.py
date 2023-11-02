def solution():
    total_fence_length = 100
    ben_paint_length = 10

    # Calculate the remaining fence length after Ben painted
    remaining_fence_length = total_fence_length - ben_paint_length

    # Calculate the length of fence that Billy painted
    billy_paint_length = remaining_fence_length / 5

    # Calculate the remaining fence length after Billy painted
    remaining_fence_length = remaining_fence_length - billy_paint_length

    # Calculate the length of fence that Johnny painted
    johnny_paint_length = remaining_fence_length / 3

    # Calculate the length of fence still needing painting
    remaining_fence_length = remaining_fence_length - johnny_paint_length

    result = remaining_fence_length
    return result

print(solution())