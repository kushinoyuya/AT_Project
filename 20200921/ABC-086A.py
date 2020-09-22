'''

【問題概要】
二つの正整数 aa, bb が与えられます。 aa と bb の積が偶数か奇数か判定してください。

【制約】
1≤a,b≤100001≤a,b≤10000
aa, bb は整数

'''
# using namespace std;

# int main() {
#     int a, b;
#     cin >> a >> b;
#     int c = a * b;
#     if (c % 2 == 0) cout << "Even" << endl;
#     else cout << "Odd" << endl;
# }

a, b = map(int, input().split())
print("Even" if a*b % 2 == 0 else "Odd")
