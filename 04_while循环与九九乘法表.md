# while 循环与循环嵌套

## 🎯 内容回顾

是时候展示真正的技术了！

在上一篇，我们学习了for循环、列表和字符串的定义、语法和一些常用方法。本文档主要内容如下：

1. 学习 while 条件循环，改进猜数字游戏。
2. 学习循环嵌套，打印九九乘法表。

## while 循环

上一篇我们学习循环的时候讲到了Python的循环有两种形式，一种计数循环也就是学过的 for 循环，那么还有另一种条件循环，就是本文档要学习的 while 循环。

while 循环其实与 if 条件分支有些相似，它们语法结构都是关键字后面接条件表达式，当条件表达式为 True 时，就执行下方的代码块。不同的地方是，条件表达式为 True 时，if 只会执行一次，而 while 会执行完整个代码块之后，又会返回来继续判断条件表达式，一直循环反复。

### while 语法

```python
while 条件表达式:
    循环体
else:
    条件为False时执行（可选）
```

### 示例：1到100求和

```python
total = 0
addend = 1
while addend <= 100:
    total += addend
    addend += 1
print('1到100各数相加的和 = ', total)  # 5050
```

**对比 for 循环：**

```python
# for 循环版本
total = 0
for i in range(1, 101):
    total += i
print(total)
```

**什么时候用 while？**
- 循环次数不确定，但有明确的结束条件
- 需要一直等待某个条件发生

### 示例：水仙花数

水仙花数：一个三位数，其各位数字立方和等于该数本身。

```python
# while 版本
num = 100
while num <= 999:
    i = num // 100      # 百位
    j = num // 10 % 10  # 十位
    k = num % 10        # 个位
    if i**3 + j**3 + k**3 == num:
        print(num)
    num += 1

# for 版本
for n in range(100, 1000):
    i, j, k = n // 100, n // 10 % 10, n % 10
    if i**3 + j**3 + k**3 == n:
        print(n)
```

### 实战：改进猜数字游戏

```python
import random

secret = random.randint(0, 100)
print("猜一个0-100之间的数字")

guess = int(input("你的猜测："))
while guess != secret:
    if guess > secret:
        print("猜大了")
    else:
        print("猜小了")
    guess = int(input("再猜一次："))

print("恭喜猜对了！")
```

### 无限循环

```python
while True:  # 永远为真，无限循环
    msg = input("说点啥（输入quit退出）：")
    if msg == "quit":
        break  # 用break跳出循环
    print(f"你说了：{msg}")
```

**什么时候用无限循环？**
- 服务器程序（7×24小时运行）
- 游戏主循环
- 需要一直等待用户输入

## 循环嵌套

循环嵌套就是在一个循环体中嵌入另一个循环。

**执行流程：**
- 外层循环执行一次，内层循环执行完整的一轮
- 外层循环再执行一次，内层循环再执行完整的一轮
- 以此类推

### 打印九九乘法表

```python
# 基础版本（有重复）
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j}*{i}={i*j}', end='\t')
    print()

# 优化版本（去重复）
for i in range(1, 10):
    for j in range(1, i + 1):  # 关键：j的范围是1到i
        print(f'{j}*{i}={i*j}', end='\t')
    print()
```

**输出：**
```
1*1=1
1*2=2   2*2=4
1*3=3   2*3=6   3*3=9
...
```

### 格式化对齐

让输出更整齐：

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i*j:2}', end='  ')  # :2 表示占2位宽度
    print()
```

### 字符串格式化速查

| 格式 | 含义 | 示例 |
|------|------|------|
| `{:2}` | 宽度为2 | `5` → ` 5` |
| `{:>2}` | 右对齐 | `5` → ` 5` |
| `{:<2}` | 左对齐 | `5` → `5 ` |
| `{:0>2}` | 左边补0 | `5` → `05` |
| `{:.2f}` | 保留2位小数 | `3.14159` → `3.14` |

## 综合实战：健壮的猜数字游戏

```python
import random

def get_valid_number(prompt):
    """获取有效的数字输入"""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("请输入数字！")

# 游戏主程序
secret = random.randint(0, 100)
print("猜一个0-100之间的数字")

attempts = 0
while True:
    guess = get_valid_number("你的猜测：")
    attempts += 1
    
    if guess == secret:
        print(f"恭喜猜对了！用了{attempts}次")
        break
    elif guess > secret:
        print("猜大了")
    else:
        print("猜小了")
```

## 🎉 文档总结

本文档我们学习了：

1. **while 循环**：条件为真就一直执行
2. **无限循环**：`while True` 配合 `break` 使用
3. **循环嵌套**：外层循环一次，内层循环一轮
4. **实战应用**：九九乘法表、健壮的猜数字游戏

**核心思路**：
- 循环次数确定 → 用 for
- 循环次数不确定 → 用 while
- 复杂问题 → 考虑循环嵌套

## 🏆 通关挑战

### 选择题

**1. 以下代码有什么问题？**
```python
tag = 'y'
for tag == 'y':
    print('好好学习')
    tag = input('继续？y/n：')
```
- A. 第1行改成 `tag=y`
- B. 第2行 `for` 改成 `while`
- C. 第3行改成 `print("我要好好学习")`
- D. 没有错误

**2. 想要输出10行10列的`*`，代码对吗？**
```python
for i in range(1, 10):
    for j in range(1, 11):
        print('*', end='')
    print()
```
- A. 第1行10改成11
- B. 第2行11改成10
- C. 第2行 range 改成 random
- D. 正确

---

🔑 **答案**：1-B, 2-A

### 编程题

**1. 求10-300以内同时能被7和8整除的整数。**

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
# 方法1：遍历判断
for num in range(10, 301):
    if num % 7 == 0 and num % 8 == 0:
        print(num)

# 方法2：直接计算（7和8的最小公倍数是56）
for num in range(56, 301, 56):
    if num >= 10:
        print(num)
```

</details>

**2. 打印1-100以内含有6的数。**

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
for num in range(1, 101):
    if '6' in str(num):
        print(num)
```

</details>

**3. 用1、2、3、4能组成多少个互不相同且无重复数字的三位数？各是多少？**

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
count = 0
for i in [1, 2, 3, 4]:
    for j in [1, 2, 3, 4]:
        for k in [1, 2, 3, 4]:
            if i != j and j != k and i != k:  # 互不相同
                print(f"{i}{j}{k}")
                count += 1
print(f"共{count}个")
```

</details>

**4. 打印金字塔（输入n=5）。**

```
    *
   ***
  *****
 *******
*********
```

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
n = int(input("输入层数："))
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
```

</details>

**5. 打印直角三角形（输入n=4）。**

```
*
**
***
****
```

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
n = int(input("输入层数："))
for i in range(1, n + 1):
    print('*' * i)
```

</details>

**6. 打印数字金字塔（输入n=4）。**

```
    1
   121
  12321
 1234321
```

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
n = int(input("输入层数："))
for i in range(1, n + 1):
    # 打印空格
    print(' ' * (n - i), end='')
    
    # 打印递增部分
    for j in range(1, i + 1):
        print(j, end='')
    
    # 打印递减部分
    for j in range(i - 1, 0, -1):
        print(j, end='')
    
    print()
```

</details>