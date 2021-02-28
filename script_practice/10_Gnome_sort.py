from typing import List

def gnome_sort(numbers: List[int])-> List[int]:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            index = index + 1
        if numbers[index] >= numbers[index - 1]:
            index = index + 1
        else:
            numbers[index],numbers[index - 1] = numbers[index - 1],numbers[index]

    return numbers


if __name__ == "__main__":
    import random
    # nums = [8,5,1,2,7,3]
    nums = [random.randint(0,1000) for _ in range(10)]
    gnome_sort(nums)
    print(gnome_sort(nums))
