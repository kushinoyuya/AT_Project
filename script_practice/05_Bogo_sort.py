'''
配列の要素をランダムに並び替えて,
運良くソートできていればソート完了というソートアルゴリズム.
配列のサイズが N で, 要素がすべて異なるとしたとき, 平均計算時間は O(N⋅N!).
処理が遅いから、なかなか使われない
'''

import random
from typing import List

#リストの中身を確認
def in_order(numbers: List[int]) -> bool:
    #処理を1行で記載した場合
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

    #処理内容の詳細
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True



def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

if __name__ == '__main__':
    nums = [random.randint(0,1000) for _ in range(10)]
    print(bogo_sort(nums))
