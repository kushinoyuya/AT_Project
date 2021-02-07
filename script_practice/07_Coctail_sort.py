#講義
from typing import List
def coctail_sort(numbers: List[int]) -> List[int]:
    #配列の数を表示させる(0~5)
    len_numbers = len(numbers)
    #
    swapped = True
    # スタートと終わりを初期値として設定する
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        # ここから、バブルソートと同じ
        for i in range(start,end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end-1,start-1,-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(coctail_sort(nums))
