'''
Big O Notation(Big o 起票)
この関数は　Ｏ（ｎ） である。」のような Ｏ の表現を突然見かけたりします。
これは、ビッグ・オー記法といって、表記を簡単にする工夫です。
議論を正確にして、かつわかりやすくするために積極的に行う略記です。
※O(n)=>forループ一回のイメージ
'''
# O(log(n))
def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)
func2(10)

# O(n)
def func3(numbers):
    for num in numbers:
        print(num)
func3([1,2,3,4,5])

# 0(n * log(n))
def func4(n):
    for i in range(int(n)):
        print(i, end='')
    print()
    if n <= 1:
        return
    func4(n/2)
func4(10)

#O(n**2)
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i],numbers[j])
        print()
func5([1,2,3,4,5])
