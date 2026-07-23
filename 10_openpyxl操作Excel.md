# 📊 自动化操作 Excel——让表格处理飞起来

## 🎯 上集回顾

上篇文章我们学习了数据库操作，掌握了如何使用 SQLite 存储和管理数据。这项技能在数据持久化方面非常强大，但有时候我们的数据来源可能是 Excel 文件，或者需要将数据导出为 Excel 格式进行分享。

今天，我们就来学习如何使用 Python 操作 Excel，让表格处理自动化、智能化！

## 🚀 openpyxl 简介

### 🎁 为什么选择 openpyxl？

Python 能操作 Excel 的库有很多：

| 库名 | 特点 | 适用场景 |
|------|------|----------|
| **openpyxl** ⭐ | 功能强大，支持读写 .xlsx 格式 | 日常办公自动化 |
| xlrd/xlwt | 老牌库，只能读/写 .xls | 旧版 Excel 文件 |
| pandas | 数据分析神器，可读写 Excel | 大数据处理 |
| xlwings | 调用 Excel 程序，保留公式 | 需要复杂公式计算 |

> 💡 **推荐**：对于大多数场景，`openpyxl` 是最佳选择！

---

### 📦 安装 openpyxl

```bash
pip install openpyxl
```

安装成功后，你会看到 `Successfully installed openpyxl` 提示。

---

### 📐 Excel 核心概念

在操作 Excel 之前，我们先来认识几个核心概念：

```
┌─────────────────────────────────────────────────────────────────┐
│                    Excel 结构层次图                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📒 工作簿 (Workbook)                                           │
│  └── 一个 Excel 文件就是一个工作簿                                │
│      │                                                          │
│      ├── 📄 工作表 1 (Sheet) - 花名册                            │
│      │   ├── 📊 行 (Row) - 横向，用数字 1, 2, 3... 表示           │
│      │   ├── 📊 列 (Column) - 纵向，用字母 A, B, C... 表示       │
│      │   └── 🔲 单元格 (Cell) - 行和列的交叉点                   │
│      │       └── 坐标 (Coordinate) - 如 B4 表示第2列第4行         │
│      │                                                          │
│      └── 📄 工作表 2 (Sheet) - 成绩单                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**⚠️ 重要提醒**：
- Excel 的索引从 **1** 开始（不是从 0 开始！）
- 列用字母表示：A, B, C... Z, AA, AB...
- 行用数字表示：1, 2, 3...
- 单元格坐标格式：**列字母 + 行数字**，如 B4

![Image 1](./images/chapter10_01.jpeg)

> 🌰 **示例**：图中【后羿】所在的位置是 **B4**，表示第 **B** 列第 **4** 行。

---

### 📂 打开 Excel 文件

**支持的文件格式**：`.xlsx` / `.xlsm` / `.xltx` / `.xltm`

> ⚠️ **注意**：`.xls` 格式（旧版 Excel）需要先转换为 `.xlsx` 才能使用 openpyxl

**示例文件**：`王者小学.xlsx`，包含两个工作表：

![Image 2](./images/chapter10_02.png)

**代码示例**：

```python
from openpyxl import load_workbook

# 文件路径（r 前缀表示原始字符串，避免转义问题）
filePath = r'D:\王者小学.xlsx'

# 打开 Excel 文件
workbook = load_workbook(filePath)

# 查看所有工作表名称
print(workbook.sheetnames)
```

![Image 3](./images/chapter10_03.png)

**运行结果**：
```
['花名册', '成绩单']
```

> 💡 **关键函数**：`load_workbook(filepath)`
> - 作用：加载已存在的 Excel 文件
> - 参数：文件路径（字符串）
> - 返回：Workbook 对象
> - ⚠️ 只能打开已存在的文件，不能创建新文件

---

## 📖 获取 Excel 数据

### 🎯 获取工作表（Sheet）

一个 Excel 文件可以包含多个工作表，获取工作表有三种常用方法：

| 方法 | 语法 | 说明 |
|------|------|------|
| **通过名称** | `workbook['表名']` | 最常用，直观明了 |
| **通过索引** | `workbook.worksheets[索引]` | 索引从 0 开始 |
| **获取活动表** | `workbook.active` | 获取当前打开时显示的表 |

**代码示例**：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)

# 方法1：通过表名获取
sheet1 = workbook["花名册"]

# 方法2：通过索引获取（从0开始）
sheet2 = workbook.worksheets[0]  # 第一个表

# 方法3：获取当前活动表
sheet3 = workbook.active

print(f"方法1: {sheet1}")
print(f"方法2: {sheet2}")
print(f"方法3: {sheet3}")
```

**运行结果**：
```
方法1: <Worksheet "花名册">
方法2: <Worksheet "花名册">
方法3: <Worksheet "成绩单">
```

> 💡 **提示**：
> - `workbook["花名册"]` 和 `workbook.worksheets[0]` 获取的是同一个表
> - `workbook.active` 获取的是 Excel 打开时默认显示的表

---

### 📏 获取表格尺寸

使用 `sheet.dimensions` 可以获取表格的数据范围：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)

sheet1 = workbook["花名册"]
sheet2 = workbook["成绩单"]

print(f"花名册: {sheet1.dimensions}")
print(f"成绩单: {sheet2.dimensions}")
```

**运行结果**：
```
花名册: A1:C5
成绩单: A1:D5
```

**含义解析**：
- `A1:C5` = 从 A1 单元格到 C5 单元格的数据区域
- `A1:D5` = 从 A1 单元格到 D5 单元格的数据区域

![Image 4](./images/chapter10_04.png)

![Image 5](./images/chapter10_05.png)

![Image 6](./images/chapter10_06.png)

> 💡 **尺寸格式**：`左上角坐标:右下角坐标`
> - 如 `A1:C5` 表示 A 列到 C 列，第 1 行到第 5 行的区域

---

### 🔲 获取单元格数据

获取单元格数据有两种常用方法：

| 方法 | 语法 | 适用场景 |
|------|------|----------|
| **坐标法** | `sheet['B2']` | 知道单元格坐标时 |
| **行列法** | `sheet.cell(row=2, column=2)` | 需要循环遍历时 |

**代码示例**：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)

sheet = workbook["花名册"]
sheet2 = workbook["成绩单"]

# 方法1：通过坐标获取
cell1 = sheet["B2"]
print(f"单元格对象: {cell1}")
print(f"单元格值: {cell1.value}")

# 方法2：通过行列获取（B2 = 第2行第2列）
cell2 = sheet.cell(row=2, column=2)
print(f"单元格值: {cell2.value}")

# 获取后羿的成绩（C4 = 第4行第3列）
score = sheet2.cell(row=4, column=3).value
print(f"后羿的成绩: {score}")
```

![Image 7](./images/chapter10_07.png)

![Image 8](./images/chapter10_08.png)

**运行结果**：
```
单元格对象: <Cell '花名册'.B2>
单元格值: 李白
单元格值: 李白
后羿的成绩: 96
```

> 💡 **总结**：
> - `sheet['B2']` → 获取单元格对象
> - `sheet['B2'].value` → 获取单元格的值
> - `sheet.cell(row=2, column=2)` → 通过行列获取（行、列从1开始）

---

### 📊 获取区域数据

#### 方法1：使用 `sheet[]`（切片语法）

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook["花名册"]

# 获取矩形区域
cells = sheet["A1:C4"]  # 从A1到C4的区域

for row in cells:       # 按行遍历
    for cell in row:    # 遍历行中的每个单元格
        print(cell.value)
```

**运行结果**：
```
学号
姓名
性别
1
李白
男
...
```

**常用切片方式**：

| 语法 | 说明 | 示例 |
|------|------|------|
| `sheet['A1:C4']` | 获取矩形区域 | A1到C4的所有单元格 |
| `sheet['A']` | 获取整列 | A列所有数据 |
| `sheet['4']` | 获取整行 | 第4行所有数据 |
| `sheet['A:C']` | 获取多列 | A到C列 |
| `sheet[2:4]` | 获取多行 | 第2到4行 |

---

#### 方法2：使用 `sheet.iter_rows()`（推荐）

`iter_rows()` 是更灵活的方法，直接用行列数字指定范围：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook["花名册"]

# 获取指定范围（第2-4行，第1-2列）
for row in sheet.iter_rows(min_row=2, max_row=4, min_col=1, max_col=2):
    for cell in row:
        print(cell.value)

# 获取所有数据
for row in sheet.iter_rows():
    for cell in row:
        print(cell.value)

# 直接获取值（不需要 .value）
for row in sheet.iter_rows(min_row=2, max_row=4, values_only=True):
    print(row)  # 直接是元组 ('1', '李白', '男')
```

**参数说明**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `min_row` | 起始行 | 1 |
| `max_row` | 结束行 | 最大行 |
| `min_col` | 起始列 | 1 |
| `max_col` | 结束列 | 最大列 |
| `values_only` | 是否只返回值 | False |

> 💡 **推荐**：需要按行列遍历时，使用 `iter_rows()` 更直观！

---

## ✏️ 修改和保存 Excel

### 修改单元格的值

修改单元格有两种方式：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook['花名册']

# 方式1：直接赋值
sheet["B2"] = '渣男教父'

# 方式2：通过 cell 对象赋值
cell = sheet["B3"]
cell.value = '蔡文姬'

# 保存文件
workbook.save(r'D:\王者小学2.xlsx')
```

![Image 11](./images/chapter10_11.png)

**对比效果**：

![Image 12](./images/chapter10_12.png)

![Image 13](./images/chapter10_13.png)

> ⚠️ **重要提醒**：
> 1. **必须保存**：修改后调用 `workbook.save(路径)` 才能生效
> 2. **另存为**：如果路径不同，会创建新文件；路径相同则覆盖原文件
> 3. **文件关闭**：保存前确保 Excel 文件已关闭，否则会报错

---

### 批量插入数据

使用 `append()` 方法可以在表格末尾批量插入数据：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook['花名册']

# 要插入的数据（列表的列表）
data = [
    ['5', '安琪拉', "女"],
    ['6', '荆轲', "女"],
    ['7', '夏侯惇', "男"],
]

# 逐行追加
for row in data:
    sheet.append(row)

workbook.save(filePath)
print("✅ 数据插入成功！")
```

![Image 14](./images/chapter10_14.png)

> 💡 **应用场景**：
> - 爬虫数据存储
> - 批量导入数据
> - 日志记录
> - 报表生成

---

## 🎯 实战项目：合并多个 Excel 文件

### 项目背景

假设你是公司的数据分析师，需要将2021年4个季度的销售数据合并成一个总表。每个季度的数据保存在单独的 Excel 文件中：

![Image 15](./images/chapter10_15.png)

### 实现思路

```
┌─────────────────────────────────────────────────────────┐
│                   数据合并流程图                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📁 2021年销售明细/                                      │
│  ├── 📄 一季度.xlsx  ──┐                                │
│  ├── 📄 二季度.xlsx  ──┼──→  🐍 Python 脚本 ──→ 📊 汇总表 │
│  ├── 📄 三季度.xlsx  ──┤         读取所有文件              │
│  └── 📄 四季度.xlsx  ──┘         提取数据                  │
│                                  合并保存                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 核心代码

```python
import os
from openpyxl import load_workbook, Workbook

# 数据文件夹路径
data_dir = r'D:\2021年销售明细'

# 创建新的工作簿保存汇总数据
summary_wb = Workbook()
summary_sheet = summary_wb.active
summary_sheet.title = "2021年销售汇总"

# 写入表头
headers = ['季度', '产品', '销量', '销售额']
summary_sheet.append(headers)

# 遍历所有Excel文件
for filename in os.listdir(data_dir):
    if filename.endswith('.xlsx'):
        # 提取季度信息
        quarter = filename.replace('.xlsx', '')
        
        # 打开文件读取数据
        file_path = os.path.join(data_dir, filename)
        wb = load_workbook(file_path)
        sheet = wb.active
        
        # 读取数据（跳过表头）
        for row in sheet.iter_rows(min_row=2, values_only=True):
            # 添加季度信息
            row_data = [quarter] + list(row)
            summary_sheet.append(row_data)
        
        wb.close()

# 保存汇总文件
summary_wb.save(r'D:\2021年销售汇总.xlsx')
print("✅ 数据合并完成！")
```

> 🎉 **恭喜你！** 至此，你已经掌握了 Python 操作 Excel 的核心技能！

---

## 📝 文档总结

### 一、核心知识点回顾

#### 1. Excel 基础概念

```
📒 工作簿 (Workbook) → 一个 Excel 文件
    └── 📄 工作表 (Sheet)
            ├── 📊 行 (Row) - 数字 1, 2, 3...
            ├── 📊 列 (Column) - 字母 A, B, C...
            └── 🔲 单元格 (Cell) - 坐标如 B4
```

**⚠️ 重要**：Excel 索引从 **1** 开始，不是 0！

#### 2. openpyxl 核心操作

| 操作 | 代码 | 说明 |
|------|------|------|
| **打开文件** | `load_workbook('文件.xlsx')` | 加载已存在的文件 |
| **获取工作表** | `wb['表名']` / `wb.worksheets[0]` | 获取指定工作表 |
| **获取单元格** | `sheet['B2']` / `sheet.cell(row=2, column=2)` | 两种获取方式 |
| **获取值** | `cell.value` | 获取单元格的值 |
| **修改值** | `sheet['B2'] = '新值'` | 直接赋值修改 |
| **批量插入** | `sheet.append([数据列表])` | 在末尾添加一行 |
| **保存文件** | `wb.save('路径.xlsx')` | 保存修改 |

#### 3. 区域数据获取方法对比

| 方法 | 优点 | 缺点 |
|------|------|------|
| `sheet['A1:C4']` | 直观，用坐标 | 需要转换行列到坐标 |
| `sheet.iter_rows()` | 直接用行列数字 | 稍微复杂一点 |

**推荐**：简单场景用 `sheet[]`，复杂遍历用 `iter_rows()`

#### 4. 完整操作流程

```python
from openpyxl import load_workbook

# 1. 打开文件
wb = load_workbook('数据.xlsx')

# 2. 获取工作表
sheet = wb['Sheet1']

# 3. 读取/修改数据
value = sheet['A1'].value
sheet['B2'] = '新数据'

# 4. 批量插入
sheet.append(['数据1', '数据2', '数据3'])

# 5. 保存文件
wb.save('数据.xlsx')
```

---

### 二、常见应用场景

1. **数据整理**：批量处理多个 Excel 文件
2. **报表生成**：自动从数据库导出数据到 Excel
3. **数据清洗**：读取 Excel 数据，处理后保存
4. **爬虫存储**：将爬取的数据保存到 Excel
5. **办公自动化**：自动填充模板、生成报告

---

### 三、学习建议

1. **多练习**：Excel 操作熟能生巧，多写代码
2. **注意索引**：时刻记住 Excel 从 1 开始计数
3. **及时保存**：修改后记得调用 `save()`
4. **关闭文件**：操作前确保 Excel 文件已关闭
5. **结合 pandas**：大数据量时考虑使用 pandas

---

### 四、下篇预告

下一篇我们将学习：
- 网络编程基础（HTTP 协议）
- 使用 requests 库发送网络请求
- API 接口调用
- 爬虫基础

掌握 Excel 操作 + 网络请求，你就可以实现数据采集 → 处理 → 存储的完整流程了！

---

## 🎮 动手练一练

光看不练假把式！下面几道题目帮你巩固今天学到的知识。

### 选择题

**1. 在 Excel 中，单元格 B3 表示？**
- A. 第 2 行第 3 列
- B. 第 3 行第 2 列
- C. 第 2 列第 3 行
- D. 第 3 列第 2 行

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：B**

**详细解析**：
- Excel 单元格坐标的格式是 **列字母 + 行数字**
- **B** 表示第 2 列（A=1, B=2, C=3...）
- **3** 表示第 3 行
- 所以 **B3** = 第 3 行第 2 列

**记忆技巧**：
- 先列后行，字母在前数字在后
- 类比坐标系：x 轴（列）在前，y 轴（行）在后

**代码对应**：
```python
# B3 的两种获取方式
sheet['B3']                    # 坐标法
sheet.cell(row=3, column=2)    # 行列法（第3行第2列）
```

</details>

---

**2. 使用 openpyxl 打开 Excel 文件，应该使用哪个函数？**
- A. `open_workbook()`
- B. `load_workbook()`
- C. `read_excel()`
- D. `open_excel()`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：B**

**详细解析**：
- 选项 A `open_workbook()`：不存在这个函数
- 选项 B `load_workbook()`：**正确**，openpyxl 中用于加载已有文件的函数
- 选项 C `read_excel()`：这是 pandas 库的函数，不是 openpyxl 的
- 选项 D `open_excel()`：不存在这个函数

**代码示例**：
```python
from openpyxl import load_workbook

# 正确用法
wb = load_workbook('数据.xlsx')

# 错误用法 ❌
wb = open_workbook('数据.xlsx')  # 函数不存在
wb = read_excel('数据.xlsx')     # 这是 pandas 的函数
```

**易混淆点**：
- openpyxl 用 `load_workbook()`
- pandas 用 `read_excel()`
- xlrd 用 `open_workbook()`

</details>

---

**3. 以下代码执行后，`value` 的值是什么？**
```python
from openpyxl import load_workbook
wb = load_workbook('王者小学.xlsx')
sheet = wb['花名册']
value = sheet.cell(row=2, column=2).value
```
- A. 学号
- B. 1
- C. 李白
- D. 男

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：C**

**详细解析**：
- `sheet.cell(row=2, column=2)` 获取第 2 行第 2 列的单元格
- 第 2 行第 2 列对应坐标 **B2**
- 根据【花名册】表格内容：
  - 第 1 行是表头：学号、姓名、性别
  - 第 2 行是：1、李白、男
- 所以第 2 行第 2 列的值是 **"李白"**

**表格结构回顾**：
```
     A      B      C
1   学号   姓名   性别
2    1     李白    男
3    2     甄姬    女
4    3     后羿    男
```

**对应关系**：
- `cell(row=2, column=2)` = B2 = "李白"
- `cell(row=2, column=1)` = A2 = "1"
- `cell(row=1, column=2)` = B1 = "姓名"

</details>

---

**4. 使用 `sheet.append()` 方法时，传入的参数应该是？**
- A. 单个值，如 `'张三'`
- B. 字典，如 `{'name': '张三', 'age': 20}`
- C. 列表，如 `['5', '张三', '男']`
- D. 元组，如 `('5', '张三', '男')`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：C**

**详细解析**：
- 选项 A 错误：`append()` 需要传入一行数据，单个值不够
- 选项 B 错误：`append()` 不接受字典类型
- 选项 C **正确**：`append()` 接受**列表**作为参数，表示一行数据
- 选项 D 虽然也能工作，但官方文档和最佳实践推荐用**列表**

**代码示例**：
```python
# ✅ 正确：传入列表
sheet.append(['5', '张三', '男'])

# ✅ 也能工作，但推荐用列表
sheet.append(('5', '张三', '男'))

# ❌ 错误：单个值
sheet.append('张三')

# ❌ 错误：字典
sheet.append({'name': '张三'})
```

**批量插入示例**：
```python
data = [
    ['5', '安琪拉', '女'],
    ['6', '荆轲', '女'],
    ['7', '夏侯惇', '男'],
]

for row in data:
    sheet.append(row)  # row 是列表
```

</details>

---

### 编程题

**1. 学生成绩统计程序**

假设你有一个【成绩单】表格，包含以下数据：

| 姓名 | 语文 | 数学 | 英语 |
|------|------|------|------|
| 李白 | 85 | 90 | 88 |
| 甄姬 | 92 | 88 | 95 |
| 后羿 | 78 | 85 | 80 |
| 瑶 | 95 | 92 | 90 |

**要求**：
1. 读取成绩单数据
2. 计算每个学生的总分和平均分
3. 将结果写入新的列（总分、平均分）
4. 找出最高分的学生并打印

<details>
<summary>🔑 参考答案与解析（点击展开）</summary>

**解题思路**：
1. 打开 Excel 文件，获取【成绩单】工作表
2. 使用 `iter_rows()` 读取数据（跳过表头）
3. 遍历每行数据，计算总分和平均分
4. 将计算结果写入新列
5. 遍历找出最高分学生
6. 保存文件

**代码实现**：

```python
from openpyxl import load_workbook

# 打开文件
filePath = r'D:\王者小学.xlsx'
wb = load_workbook(filePath)
sheet = wb['成绩单']

print("🚀 开始处理成绩数据...\n")

# 添加表头
sheet['E1'] = '总分'
sheet['F1'] = '平均分'

# 存储学生成绩信息
students = []

# 读取数据并计算（从第2行开始，跳过表头）
for row in sheet.iter_rows(min_row=2, max_row=5, values_only=True):
    name, chinese, math, english = row[0], row[1], row[2], row[3]
    
    # 计算总分和平均分
    total = chinese + math + english
    average = total / 3
    
    # 保存学生信息
    students.append({
        'name': name,
        'total': total,
        'average': average
    })
    
    print(f"📊 {name}: 语文{chinese} 数学{math} 英语{english} → 总分{total} 平均分{average:.2f}")

# 将结果写回Excel
for i, student in enumerate(students, start=2):
    sheet.cell(row=i, column=5).value = student['total']      # E列
    sheet.cell(row=i, column=6).value = round(student['average'], 2)  # F列

# 找出最高分学生
top_student = max(students, key=lambda x: x['total'])
print(f"\n🏆 最高分学生: {top_student['name']}")
print(f"   总分: {top_student['total']}")
print(f"   平均分: {top_student['average']:.2f}")

# 保存文件
wb.save(filePath)
print(f"\n✅ 处理完成，结果已保存到 {filePath}")
```

**运行结果**：
```
🚀 开始处理成绩数据...

📊 李白: 语文85 数学90 英语88 → 总分263 平均分87.67
📊 甄姬: 语文92 数学88 英语95 → 总分275 平均分91.67
📊 后羿: 语文78 数学85 英语80 → 总分243 平均分81.00
📊 瑶: 语文95 数学92 英语90 → 总分277 平均分92.33

🏆 最高分学生: 瑶
   总分: 277
   平均分: 92.33

✅ 处理完成，结果已保存到 D:\王者小学.xlsx
```

**知识点总结**：
- `iter_rows(values_only=True)` 直接获取值
- `sheet.cell(row, column).value` 写入数据
- `max()` 函数配合 `key` 参数找出最大值
- 注意行号从 2 开始（跳过表头）

**进阶挑战**：
- 添加排名列
- 按总分降序排列
- 计算各科班级平均分
- 将结果导出为新文件

</details>

---

**2. 多文件数据汇总**

假设你有 3 个班级的成绩文件：
- 一班.xlsx
- 二班.xlsx
- 三班.xlsx

每个文件结构相同：
| 姓名 | 语文 | 数学 | 英语 |

**要求**：
1. 读取所有班级的数据
2. 合并到一个新的 Excel 文件中
3. 添加"班级"列标识数据来源
4. 计算每个班级的平均成绩

<details>
<summary>🔑 参考答案与解析（点击展开）</summary>

**解题思路**：
1. 导入必要的库（os、openpyxl）
2. 创建新的工作簿用于保存汇总数据
3. 遍历数据文件夹中的所有 .xlsx 文件
4. 对每个文件：
   - 提取班级名称（从文件名）
   - 读取数据
   - 添加班级标识
   - 追加到汇总表
5. 计算各班级平均分
6. 保存汇总文件

**代码实现**：

```python
import os
from openpyxl import load_workbook, Workbook

def merge_class_data(data_dir, output_file):
    """
    合并多个班级的成绩数据
    
    参数:
        data_dir: 数据文件夹路径
        output_file: 输出文件路径
    """
    # 创建新的工作簿
    wb = Workbook()
    sheet = wb.active
    sheet.title = "成绩汇总"
    
    # 写入表头
    headers = ['班级', '姓名', '语文', '数学', '英语', '总分']
    sheet.append(headers)
    
    # 存储各班统计数据
    class_stats = {}
    
    print("🚀 开始合并数据...\n")
    
    # 遍历数据文件夹
    for filename in os.listdir(data_dir):
        if filename.endswith('.xlsx'):
            # 提取班级名称
            class_name = filename.replace('.xlsx', '')
            print(f"📂 正在处理: {filename}")
            
            # 打开文件
            file_path = os.path.join(data_dir, filename)
            wb_source = load_workbook(file_path)
            source_sheet = wb_source.active
            
            # 初始化班级统计
            class_stats[class_name] = {
                'count': 0,
                'chinese_sum': 0,
                'math_sum': 0,
                'english_sum': 0
            }
            
            # 读取数据（跳过表头）
            for row in source_sheet.iter_rows(min_row=2, values_only=True):
                name, chinese, math, english = row
                total = chinese + math + english
                
                # 添加到汇总表
                sheet.append([class_name, name, chinese, math, english, total])
                
                # 更新统计
                class_stats[class_name]['count'] += 1
                class_stats[class_name]['chinese_sum'] += chinese
                class_stats[class_name]['math_sum'] += math
                class_stats[class_name]['english_sum'] += english
            
            wb_source.close()
    
    # 保存汇总数据
    wb.save(output_file)
    
    # 打印统计结果
    print("\n" + "=" * 60)
    print("📊 各班平均成绩统计")
    print("=" * 60)
    print(f"{'班级':<10}{'人数':<8}{'语文':<8}{'数学':<8}{'英语':<8}")
    print("-" * 60)
    
    for class_name, stats in class_stats.items():
        count = stats['count']
        avg_chinese = stats['chinese_sum'] / count
        avg_math = stats['math_sum'] / count
        avg_english = stats['english_sum'] / count
        
        print(f"{class_name:<10}{count:<8}{avg_chinese:<8.2f}{avg_math:<8.2f}{avg_english:<8.2f}")
    
    print("=" * 60)
    print(f"\n✅ 数据合并完成！")
    print(f"📁 汇总文件: {output_file}")
    print(f"📊 总记录数: {sum(s['count'] for s in class_stats.values())}")


# 使用示例
if __name__ == '__main__':
    data_directory = r'D:\班级成绩'  # 数据文件夹
    output_path = r'D:\成绩汇总.xlsx'  # 输出文件
    
    merge_class_data(data_directory, output_path)
```

**运行结果**：
```
🚀 开始合并数据...

📂 正在处理: 一班.xlsx
📂 正在处理: 二班.xlsx
📂 正在处理: 三班.xlsx

============================================================
📊 各班平均成绩统计
============================================================
班级      人数    语文    数学    英语    
------------------------------------------------------------
一班      45      85.50   88.20   86.70   
二班      42      87.30   85.60   89.10   
三班      44      84.80   90.20   87.50   
============================================================

✅ 数据合并完成！
📁 汇总文件: D:\成绩汇总.xlsx
📊 总记录数: 131
```

**知识点总结**：
- `os.listdir()` 遍历文件夹
- `os.path.join()` 拼接路径
- `Workbook()` 创建新工作簿
- 批量处理多个文件
- 数据统计和计算

**进阶挑战**：
- 添加年级排名
- 找出各班第一名
- 生成图表可视化
- 添加数据验证

</details>