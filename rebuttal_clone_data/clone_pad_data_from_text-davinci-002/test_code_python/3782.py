def solution():
    bucket_seashells = 1
    jar_seashells = bucket_seashells / 5
    bag_seashells = jar_seashells / 3
    total_seashells = bucket_seashells + jar_seashells + bag_seashells
    result = total_seashells
    return result

print(solution())