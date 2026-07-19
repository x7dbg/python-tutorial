# 猜数字小游戏

## 🎯 内容回顾

趁热打铁，做几道题巩固一下！

先来波回忆杀，看看上一篇我们搞了啥：介绍了为什么选择学习Python，学习了Python的语法基础，还认识了在Python编码过程中经常会不小心犯的错误，这些内容都非常的简单易懂，有些同学已经按捺不住要编码想要大干一场了，作为过来人表示很理解，但冰冻三尺非一日之寒，编程之路不会一蹴而就。

废话不多说，开干。本文档，我们的目标是尝试编写一个简单的猜数字小游戏。

下面是本文档的主要内容：

1. 学习Python的数值类型：整数(int)、浮点数(float)、布尔(bool)，以及类型转换。
2. 学习四类运算符：算术、赋值、比较、逻辑。
3. 学习 if 条件分支语句，完成猜数字游戏。

---

实战时间到！

<details>
<summary>点击查看参考代码</summary>

```python
# 参考代码（待补充）

```

**思路解析**：

（解析待补充）

</details>

## 数值类型

Python 有4种数值类型：

| 类型 | 说明 | 示例 |
|------|------|------|
| int | 整数 | 10, -5, 0 |
| float | 浮点数（小数） | 3.14, -0.5 |
| bool | 布尔值 | True, False |
| complex | 复数 | 3+4j（很少用） |

### 整数和浮点数

```python
# 整数运算
a = 10
b = 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...（除法结果永远是浮点数）
print(a // b)   # 3（整除，向下取整）
print(a % b)    # 1（取余）
print(a ** b)   # 1000（10的3次方）

# 浮点数
pi = 3.14159
print(pi * 2)   # 6.28318

# 科学计数法
big_num = 1.5e6   # 1500000
small_num = 1.5e-6  # 0.0000015
```

### 布尔类型

布尔值只有两个：`True`（真）和 `False`（假）。

```python
# 布尔值可以参与运算
print(True + 1)   # 2（True当作1）
print(False + 1)  # 1（False当作0）

# 比较运算返回布尔值
print(5 > 3)      # True
print(5 == 3)     # False
```

**哪些值为False？**
- `False`、`None`
- `0`、`0.0`、`0j`（零）
- `''`、`[]`、`{}`、`()`（空字符串、空列表、空字典、空元组）

其他都是True。

### 类型转换

```python
# 显式转换
print(int(3.7))      # 3（截断小数部分）
print(float(5))      # 5.0
print(bool(0))       # False
print(bool(100))     # True

# 隐式转换（运算时自动转换）
result = 5 + 3.0     # 结果是 8.0（整数自动转浮点数）
```

## 运算符

### 算术运算符

| 运算符 | 作用 | 示例 |
|--------|------|------|
| + | 加 | 5 + 3 = 8 |
| - | 减 | 5 - 3 = 2 |
| * | 乘 | 5 * 3 = 15 |
| / | 除 | 5 / 2 = 2.5 |
| // | 整除 | 5 // 2 = 2 |
| % | 取余 | 5 % 2 = 1 |
| ** | 幂 | 2 ** 3 = 8 |

```python
# 实际应用
minutes = 125
hours = minutes // 60      # 2小时
remaining = minutes % 60   # 5分钟
print(f"{minutes}分钟 = {hours}小时{remaining}分钟")
```

### 赋值运算符

```python
x = 10
x += 5      # 等同于 x = x + 5，x现在是15
x -= 3      # 等同于 x = x - 3，x现在是12
x *= 2      # 等同于 x = x * 2，x现在是24
x /= 4      # 等同于 x = x / 4，x现在是6.0
```

### 比较运算符

| 运算符 | 含义 |
|--------|------|
| == | 等于 |
| != | 不等于 |
| > | 大于 |
| < | 小于 |
| >= | 大于等于 |
| <= | 小于等于 |

```python
age = 18
print(age >= 18)      # True
print(age == 20)      # False
print(age != 20)      # True
```

### 逻辑运算符

| 运算符 | 含义 | 示例 |
|--------|------|------|
| and | 与 | True and False → False |
| or | 或 | True or False → True |
| not | 非 | not True → False |

```python
# 判断年龄是否在18到60之间
age = 25
if age >= 18 and age <= 60:
    print("是劳动力")

# 判断是否是周末
day = "周六"
if day == "周六" or day == "周日":
    print("周末愉快！")
```

### 运算符优先级

不用死记硬背，记住：**括号 > 幂运算 > 乘除 > 加减 > 比较 > 逻辑**

```python
result = 2 + 3 * 4        # 14（先乘后加）
result = (2 + 3) * 4      # 20（括号优先）
result = 2 ** 3 + 1       # 9（先幂运算）
```

## 条件分支语句

### 基本 if 语句

```python
age = 20
if age >= 18:
    print("已成年")
```

### if-else 结构

```python
age = 16
if age >= 18:
    print("已成年")
else:
    print("未成年")
```

### if-elif-else 结构

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"成绩等级：{grade}")
```

### 嵌套 if

```python
is_member = True
amount = 150

if is_member:
    if amount >= 100:
        discount = 0.8
    else:
        discount = 0.9
else:
    discount = 1.0

print(f"折扣：{discount}")
```

## 实战：猜数字游戏

现在用学到的知识完成猜数字游戏：

```python
import random

# 生成0-100的随机数
secret = random.randint(0, 100)

print("猜一个0-100之间的数字")

guess = int(input("你的猜测："))

if guess == secret:
    print("恭喜猜对了！")
elif guess > secret:
    print("猜大了")
else:
    print("猜小了")

print(f"正确答案是：{secret}")
```

**改进版**（可以一直猜直到猜对）：

```python
import random

secret = random.randint(0, 100)
attempts = 0

print("猜一个0-100之间的数字")

while True:
    guess = int(input("你的猜测："))
    attempts += 1
    
    if guess == secret:
        print(f"恭喜猜对了！用了{attempts}次")
        break
    elif guess > secret:
        print("猜大了，再试试")
    else:
        print("猜小了，再试试")
```

## 🏆 通关挑战

光看不练假把式，来几道题热热身！

### 选择题

**1. 以下哪个表达式的结果为True？**
- A. `5 > 3 and 2 > 4`
- B. `5 > 3 or 2 > 4`
- C. `not 5 > 3`
- D. `5 == '5'`

**2. 执行 `17 // 4` 的结果是？**
- A. 4.25
- B. 4
- C. 1
- D. 5

**3. 以下代码的输出是？**
```python
x = 5
x += 3
x *= 2
print(x)
```
- A. 16
- B. 13
- C. 11
- D. 26

**4. 哪个运算符用于判断两个值是否相等？**
- A. `=`
- B. `==`
- C. `===`
- D. `!=`

---

🔑 **答案揭秘**：

<details>
<summary>点击查看答案</summary>

**答案**：
1. **B** - `or` 只要有一个为True结果就是True
2. **B** - `//` 是整除，17除以4等于4余1
3. **A** - x先变成8，再乘以2得16
4. **B** - `==` 是比较，`=` 是赋值

</details>

### 编程题

**1. 编写程序，输入三个数字，输出其中的最大值。**

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
# 方法1：使用if-else
a = float(input("输入第一个数："))
b = float(input("输入第二个数："))
c = float(input("输入第三个数："))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

print(f"最大值是：{max_num}")

# 方法2：使用内置函数（更简单）
max_num = max(a, b, c)
print(f"最大值是：{max_num}")
```

</details>

**2. 编写程序，输入年份，判断是否是闰年。**

闰年判断规则：
- 能被4整除但不能被100整除，或者
- 能被400整除

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
year = int(input("输入年份："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")
```

</details>

**3. 编写简易计算器，支持加减乘除。**

---

🔑 **参考实现**：

<details>
<summary>点击查看代码</summary>

```python
num1 = float(input("输入第一个数："))
operator = input("输入运算符(+ - * /)：")
num2 = float(input("输入第二个数："))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = "错误：除数不能为0"
    else:
        result = num1 / num2
else:
    result = "错误：未知的运算符"

print(f"结果：{result}")
```

</details>

## 🎉 文档总结

本文档我们学习了：

1. **数值类型**：int、float、bool，以及类型转换
2. **运算符**：算术、赋值、比较、逻辑四类运算符
3. **条件分支**：if、if-else、if-elif-else 三种结构
4. **实战案例**：猜数字游戏

**核心思路**：
- 用变量存储数据
- 用运算符处理数据
- 用条件分支控制程序流程

**下篇预告**：
我们将学习循环语句，让程序可以重复执行代码，实现更强大的功能！