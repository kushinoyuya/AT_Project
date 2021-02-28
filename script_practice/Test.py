################## Bubble Sort
# def bubble_sort(numbers):
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers -1 -i):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     return numbers
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0,1000) for i in range(10)]
#     bubble_sort(nums)
#     print(bubble_sort(nums))
################## Coctail Sort
# def coctail_sort(numbers):
#     len_numbers = len(numbers)
#     swapped = True
#     start = 0
#     end = len_numbers - 1
#     while swapped:
#         swapped = False
#         for i in range(start,end):
#             if numbers[i] > numbers[i+1]:
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#                 swapped = True
#         if not swapped:
#             break
#         swapped = False
#         end = end - 1
#         for i in range(end-1, start-1, -1):
#             if numbers[i] > numbers[i + 1]:
#                 numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#                 swapped = True
#         start = start + 1
#     return numbers
# if __name__ == "__main__":
#     import random
#     num = [random.randint(0,1000) for _ in range(10)]
#     print(coctail_sort(num))
################## Comb Sort
# def comb_sort(numbers):
#     len_numbers = len(numbers)
#     gap = len_numbers
#     swapped = True
#     while gap != 1:
#         gap = int(gap / 1.3)
#         if gap < 1:
#             gap - 1
#         swapped = False
#         for i in range(0, len_numbers - gap):
#             if numbers[i] > numbers[i + gap]:
#                 numbers[i], numbers[i+gap]=numbers[i+gap],numbers[i]
#                 swapped = True
#             pass
#     return numbers
# if __name__ == "__main__":
#     import random
#     nums = [random.randint(0,1000) for _ in range(10)]
#     comb_sort(nums)
#     print(comb_sort(nums))
################## Selection Sort
# def selection_sort(numbers):
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             for j in range(i+1, len_numbers):
#                 if numbers[min_idx] > numbers[j]:
#                     min_idx
#         numbers[i],numbers[min_idx] > numbers[min_idx],numbers[i]
#     return numbers
# if __name__ == "__main__":
#     import random
#     nums = [random.randint(0,1000) for _ in range(10)]
#     selection_sort(nums)
#     print(selection_sort(nums))
