
#擬似コード
# ①まず左はしの数をA[n] とします。
# ②一つ右隣の数値は、A[n+1]としましょう。
# ③A[n]とA[n+1]を比べて、A[n+1]が大きい場合は、A[n]とA[n+1]の数値を交換(スワップ)します。
# ①の１つ右の数に移動して、①～③の手順が数値の並び替えが終わるまで繰り返されます。

#予習
# def bubble_sort(numbers):
#     for i in range(len(numbers)):
#         for j in range(len(numbers)-1,i,-1):
#             if numbers[j] < numbers[j-1]:
#                 num[j], num[j-1] = num[j-1], num[j]
#         return numbers



#講義
from typing import List
def bubble_sort(numbers: List[int]) -> List[int]:
    #配列の数を表示させる(0~5)
    len_numbers = len(numbers)
    # print(len_numbers)
    #配列の数をリストにする
    for i in range(len_numbers):
        #末端配列(5番目のリストを左に１つずらす)
        #最初は (len_numbers -1 -i) => (6 -1 -0)
        for j in range(len_numbers -1 -i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == '__main__':
    # nums = [2,5,1,8,7,3]
    import random
    nums = [random.randint(0,1000) for i in range(10)]
    bubble_sort(nums)
    print(bubble_sort(nums))
