def solution():
    directx_owned_by_microsoft = True
    linux_kernel_creator = "Linus Torvalds"
    linux_competes_with_windows = True

    if linux_kernel_creator != "Microsoft" and not directx_owned_by_microsoft and linux_competes_with_windows:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())