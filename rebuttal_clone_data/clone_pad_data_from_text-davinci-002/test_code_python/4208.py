def solution():
     pages_with_images = 98 / 2
     pages_with_introduction = 11
     pages_filled = pages_with_images + pages_with_introduction
     pages_remaining = 98 - pages_filled
     pages_with_text = pages_remaining / 2
     result = pages_with_text
     return result

print(solution())