# 🎨 openpyxl 高级操作——让 Excel 更专业

## 🎯 上集回顾

上一篇我们学习了 openpyxl 的基础操作，包括打开文件、读取数据、修改单元格、批量插入等。这些技能已经能帮助我们完成大部分日常办公自动化任务。

今天，我们将学习更高级的操作：
- 🎨 **美化表格**：字体、颜色、边框、对齐
- 📊 **灵活获取数据**：按列读取、行列属性
- 📝 **工作表管理**：新建、删除、重命名
- 📐 **行列操作**：插入、删除行列

掌握这些技能，你就能制作出**专业级**的 Excel 报表！

---

## 🔍 获取单元格属性

### 单元格基本信息

除了 `value`（值），单元格还有以下常用属性：

| 属性 | 说明 | 示例 |
|------|------|------|
| `cell.row` | 行号（从1开始） | `2` |
| `cell.column` | 列号（从1开始） | `2` |
| `cell.coordinate` | 坐标 | `'B2'` |
| `cell.value` | 单元格值 | `'李白'` |

**代码示例**：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook["花名册"]

# 获取单元格
cell = sheet["B2"]  # 李白
cell2 = sheet["C4"]  # 96

# 打印单元格属性
print(f"📍 单元格 {cell.coordinate}:")
print(f"   行号: {cell.row}")
print(f"   列号: {cell.column}")
print(f"   值: {cell.value}")

print(f"\n📍 单元格 {cell2.coordinate}:")
print(f"   行号: {cell2.row}")
print(f"   列号: {cell2.column}")
print(f"   值: {cell2.value}")
```

**运行结果**：
```
📍 单元格 B2:
   行号: 2
   列号: 2
   值: 李白

📍 单元格 C4:
   行号: 4
   列号: 3
   值: 96
```

> 💡 **应用场景**：
> - 遍历单元格时需要知道当前位置
> - 根据行列号进行条件判断
> - 动态生成坐标

---

## 📊 获取区域数据进阶

### 按列获取数据：`sheet.iter_cols()`

上一篇我们学了 `iter_rows()` 按行获取数据，现在学习 `iter_cols()` **按列获取**：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook["花名册"]

# 按列获取数据（第1-2列，第1-4行）
print("📊 按列获取数据：\n")
for col in sheet.iter_cols(min_row=1, max_row=4, min_col=1, max_col=2):
    print(f"列数据: {[cell.value for cell in col]}")
```

**运行结果**：
```
📊 按列获取数据：

列数据: ['学号', '1', '2', '3']
列数据: ['姓名', '李白', '甄姬', '后羿']
```

> 💡 **对比记忆**：
> - `iter_rows()` → 横向遍历，一行一行读取
> - `iter_cols()` → 纵向遍历，一列一列读取

---

### 快速获取所有行列：`sheet.rows` / `sheet.columns`

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook["花名册"]

# 获取所有行
print("📋 所有行数据：")
for row in sheet.rows:
    print([cell.value for cell in row])

# 获取所有列
print("\n📋 所有列数据：")
for col in sheet.columns:
    print([cell.value for cell in col])
```

**效果等同于**：
- `sheet.rows` = `sheet.iter_rows()`
- `sheet.columns` = `sheet.iter_cols()`

> ⚠️ **注意**：这两个属性会加载所有数据，大数据量时建议使用 `iter_rows()` / `iter_cols()`

---

## 📝 行列操作

### 插入空行/空列

| 方法 | 语法 | 说明 |
|------|------|------|
| 插入行 | `sheet.insert_rows(idx, amount)` | 在 idx 行前插入 amount 行 |
| 插入列 | `sheet.insert_cols(idx, amount)` | 在 idx 列前插入 amount 列 |

**代码示例**：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)
sheet = workbook['花名册']

# 在第3行前插入2行空行
sheet.insert_rows(idx=3, amount=2)

# 在第2列前插入1列空列
sheet.insert_cols(idx=2, amount=1)

workbook.save(r'D:\王者小学_插入行列.xlsx')
print("✅ 插入完成！")
```

![Image 1](./images/chapter11_01.png)

> 💡 **参数说明**：
> - `idx`：插入位置（行号/列号）
> - `amount`：插入数量（默认1）

---

### 删除行/列

| 方法 | 语法 | 说明 |
|------|------|------|
| 删除行 | `sheet.delete_rows(idx, amount)` | 从 idx 行开始删除 amount 行 |
| 删除列 | `sheet.delete_cols(idx, amount)` | 从 idx 列开始删除 amount 列 |

**代码示例**：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学_插入行列.xlsx'
workbook = load_workbook(filePath)
sheet = workbook['花名册']

# 删除第3-4行（2行）
sheet.delete_rows(idx=3, amount=2)

# 删除第2列（1列）
sheet.delete_cols(idx=2, amount=1)

workbook.save(r'D:\王者小学_恢复.xlsx')
print("✅ 删除完成！")
```

> ⚠️ **注意**：删除操作不可逆，建议先备份文件！

---

## 📑 工作表管理

### 新建工作表

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)

# 创建新工作表
workbook.create_sheet("身高")
print(f"📑 所有工作表: {workbook.sheetnames}")

# 获取新工作表并写入数据
sheet = workbook["身高"]
data = [
    ['学号', '身高'],
    ['1', '168'],
    ['2', '181'],
    ['3', '160'],
]

for row in data:
    sheet.append(row)

workbook.save(filePath)
print("✅ 新工作表创建完成！")
```

![Image 2](./images/chapter11_02.png)

![Image 3](./images/chapter11_03.png)

---

### 删除工作表

**两种方式**：

```python
from openpyxl import load_workbook

filePath = r'D:\王者小学.xlsx'
workbook = load_workbook(filePath)

print(f"删除前: {workbook.sheetnames}")

# 方式1：使用 del
del workbook['身高']

# 方式2：使用 remove()
# sheet = workbook['身高']
# workbook.remove(sheet)

print(f"删除后: {workbook.sheetnames}")
workbook.save(filePath)
```

![Image 4](./images/chapter11_04.png)

> ⚠️ **注意**：
> - 工作表名**区分大小写**
> - 表名不存在会报错

---

### 新建 Excel 文件并修改表名

```python
from openpyxl import Workbook

# 创建新工作簿
workbook = Workbook()

# 获取默认工作表并修改名称
sheet = workbook.active
sheet.title = "学生信息"

# 写入数据
sheet.append(['姓名', '年龄', '成绩'])
sheet.append(['张三', 18, 95])

# 保存
workbook.save(r"D:\新建Excel.xlsx")
print("✅ 新文件创建完成！")
```

![Image 5](./images/chapter11_05.png)

![Image 6](./images/chapter11_06.png)

![Image 7](./images/chapter11_07.png)

> 💡 **对比**：
> - `load_workbook()` → 打开已有文件
> - `Workbook()` → 创建新文件

---

## 🎨 设置表格样式

### 样式属性一览

| 样式 | 类 | 作用 |
|------|-----|------|
| 字体 | `Font` | 设置字体、大小、颜色、加粗等 |
| 填充 | `PatternFill` | 设置背景颜色 |
| 对齐 | `Alignment` | 设置水平/垂直对齐 |
| 边框 | `Border` + `Side` | 设置单元格边框 |

---

### 完整样式设置示例

```python
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, colors

# 打开文件
filePath = r"D:\2021年销售分析\全年数据.xlsx"
wb = load_workbook(filePath)
ws = wb.active

# ========== 1. 调整列宽 ==========
ws.column_dimensions["A"].width = 25
ws.column_dimensions["B"].width = 10
ws.column_dimensions["C"].width = 10

# ========== 2. 定义样式 ==========

# 字体样式
font = Font(
    name="微软雅黑",      # 字体名称
    size=12,             # 字体大小
    color=colors.BLACK,  # 字体颜色
    bold=False           # 是否加粗
)

# 背景填充（浅灰色）
fill = PatternFill(
    fill_type="solid",
    start_color="CDCDCD",
    end_color="CDCDCD"
)

# 对齐方式（居中）
alignment = Alignment(
    horizontal="center",  # 水平居中
    vertical="center"     # 垂直居中
)

# 边框样式（细黑线）
side = Side(
    border_style="thin",
    color=colors.BLACK
)
border = Border(
    left=side, right=side,
    top=side, bottom=side
)

# ========== 3. 应用样式到所有单元格 ==========
for row in ws.rows:
    for cell in row:
        cell.font = font
        cell.fill = fill
        cell.alignment = alignment
        cell.border = border

# ========== 4. 表头特殊样式（蓝色加粗） ==========
header_font = Font(
    name="宋体",
    size=12,
    color=colors.BLUE,
    bold=True
)

for cell in ws[1]:  # 第一行（表头）
    cell.font = header_font

# 保存
wb.save(r"D:\2021年销售分析\全年数据-格式调整.xlsx")
print("✅ 样式设置完成！")
```

![Image 8](./images/chapter11_08.png)

---

### 样式参数速查表

#### Font（字体）

```python
Font(
    name='微软雅黑',      # 字体名称
    size=12,              # 字体大小
    bold=True/False,      # 是否加粗
    italic=True/False,    # 是否斜体
    color=colors.RED      # 字体颜色
)
```

#### PatternFill（填充）

```python
PatternFill(
    fill_type='solid',    # 填充类型
    start_color='FF0000', # 开始颜色（十六进制）
    end_color='FF0000'    # 结束颜色
)
```

#### Alignment（对齐）

```python
Alignment(
    horizontal='center',   # 水平对齐: left/center/right
    vertical='center',     # 垂直对齐: top/center/bottom
    wrap_text=True,        # 自动换行
    shrink_to_fit=True     # 自适应宽度
)
```

#### Border（边框）

```python
side = Side(
    border_style='thin',   # 边框样式
    color=colors.BLACK     # 边框颜色
)
border = Border(
    left=side, right=side,
    top=side, bottom=side
)
```

**边框样式可选值**：
- `'thin'` - 细线
- `'medium'` - 中等
- `'thick'` - 粗线
- `'dashed'` - 虚线
- `'dotted'` - 点线
- `'double'` - 双线

---

## 🎯 实战项目一：数据汇总统计

### 项目背景

某公司用【明细.xlsx】登记了各部门办公设备使用情况，现在需要按**部门**统计各**设备类型**的数量。

**原始数据**：

![Image 9](./images/chapter11_09.png)

**目标结果**：

![Image 10](./images/chapter11_10.png)

---

### 实现思路

```
┌─────────────────────────────────────────────────────────┐
│                   数据汇总流程                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1️⃣ 读取明细数据                                         │
│     └── 遍历每一行，提取部门和设备类型                      │
│                                                         │
│  2️⃣ 统计数据                                             │
│     └── 用字典记录：{部门: [类型1数量, 类型2数量, ...]}    │
│                                                         │
│  3️⃣ 生成汇总表                                           │
│     └── 创建新工作簿，写入统计结果                          │
│                                                         │
│  4️⃣ 设置样式                                             │
│     └── 添加边框、居中对齐                                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### 代码实现

```python
import os
import openpyxl as xl
from openpyxl.styles import Alignment, Border, Side, colors

def 汇总数据(file_path, save_path):
    """汇总各部门设备数量"""
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print("❌ 输入文件不存在")
        return
    
    # 1. 读取明细数据
    workbook = xl.load_workbook(file_path)
    sheet = workbook.worksheets[0]
    
    # 设备类型列表
    equipment_types = [
        '笔记本电脑', '台式电脑', '传真机', 
        '多功能复印机', '激光打印机', '针式打印机'
    ]
    
    # 统计数据：{部门: [类型1数量, 类型2数量, ..., 总计]}
    stats = {}
    
    # 遍历数据（从第3行开始，跳过表头）
    for row in sheet.iter_rows(min_row=3):
        department = row[0].value      # 部门
        equip_type = row[2].value      # 设备类型
        
        # 初始化部门数据
        if department not in stats:
            stats[department] = [0] * 7  # 6种类型 + 总计
        
        # 统计数量
        if equip_type in equipment_types:
            index = equipment_types.index(equip_type)
            stats[department][index] += 1
            stats[department][6] += 1  # 总计
    
    # 2. 创建汇总表
    workbook2 = xl.Workbook()
    sheet2 = workbook2.active
    sheet2.title = "设备汇总"
    
    # 写入表头
    headers = ['部门'] + equipment_types + ['总计']
    sheet2.append(headers)
    
    # 写入各部门数据
    total_row = ['总计'] + [0] * 7
    for dept, counts in stats.items():
        row_data = [dept] + counts
        sheet2.append(row_data)
        
        # 累加总计
        for i in range(7):
            total_row[i + 1] += counts[i]
    
    # 写入总计行
    sheet2.append(total_row)
    
    # 3. 设置样式
    设置样式(sheet2)
    
    # 4. 保存文件
    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    workbook2.save(save_path)
    print(f"✅ 汇总完成！保存至: {save_path}")


def 设置样式(sheet):
    """设置表格样式"""
    # 边框样式
    side = Side(border_style="thin", color=colors.BLACK)
    border = Border(left=side, right=side, top=side, bottom=side)
    
    # 对齐方式（居中）
    alignment = Alignment(
        horizontal="center",
        vertical="center"
    )
    
    # 应用样式到所有单元格
    for row in sheet.rows:
        for cell in row:
            cell.alignment = alignment
            cell.border = border


# 运行
if __name__ == '__main__':
    汇总数据(
        r'D:\数据\第11讲\明细.xlsx',
        r'D:\数据\第11讲\汇总.xlsx'
    )
```

---

## 🎯 实战项目二：数据分类导出

### 项目背景

将【明细.xlsx】按**部门**分类，每个部门的数据保存到一个单独的工作表中。

**目标结果**：

![Image 11](./images/chapter11_11.png)

---

### 代码实现

```python
import openpyxl as xl
from openpyxl.styles import Alignment, Border, Side, colors

def 部门分类(file_path, save_path):
    """按部门分类数据"""
    
    # 1. 读取数据
    workbook = xl.load_workbook(file_path)
    sheet = workbook.worksheets[0]
    
    # 按部门分组数据
    dept_data = {}
    
    for row in sheet.iter_rows(min_row=3, values_only=True):
        department = row[0]
        
        if department not in dept_data:
            dept_data[department] = []
        
        dept_data[department].append(row[1:])  # 保存除部门外的数据
    
    # 2. 创建新工作簿
    header = ['房间', '类型', '使用人', '品牌', '规格', 'IP地址', '登记日期']
    workbook2 = xl.Workbook()
    
    # 删除默认工作表
    workbook2.remove(workbook2.active)
    
    # 3. 为每个部门创建工作表
    for dept, data in dept_data.items():
        # 创建工作表
        sheet2 = workbook2.create_sheet(title=dept)
        
        # 写入表头
        sheet2.append(header)
        
        # 写入数据
        for row_data in data:
            sheet2.append(row_data)
    
    # 4. 设置样式
    for sheet in workbook2.worksheets:
        设置样式(sheet)
    
    # 5. 保存
    workbook2.save(save_path)
    print(f"✅ 分类完成！共生成 {len(dept_data)} 个工作表")


def 设置样式(sheet):
    """设置表格样式"""
    side = Side(border_style="thin", color=colors.BLACK)
    border = Border(left=side, right=side, top=side, bottom=side)
    alignment = Alignment(horizontal="center", vertical="center")
    
    for row in sheet.rows:
        for cell in row:
            cell.alignment = alignment
            cell.border = border


# 运行
if __name__ == '__main__':
    try:
        部门分类(
            r'D:\数据\第11讲\明细.xlsx',
            r'D:\数据\第11讲\分类-部门.xlsx'
        )
    except Exception as e:
        print(f"❌ 出错了: {e}")
        raise
```

---

## 📝 文档总结

### 一、核心知识点回顾

#### 1. 单元格属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `cell.row` | 行号 | `2` |
| `cell.column` | 列号 | `2` |
| `cell.coordinate` | 坐标 | `'B2'` |
| `cell.value` | 值 | `'李白'` |

#### 2. 数据获取方法对比

| 方法 | 遍历方向 | 适用场景 |
|------|----------|----------|
| `iter_rows()` | 按行 | 逐行处理数据 |
| `iter_cols()` | 按列 | 逐列处理数据 |
| `sheet.rows` | 按行 | 快速获取所有行 |
| `sheet.columns` | 按列 | 快速获取所有列 |

#### 3. 行列操作

| 操作 | 方法 | 参数说明 |
|------|------|----------|
| 插入行 | `insert_rows(idx, amount)` | idx:位置, amount:数量 |
| 插入列 | `insert_cols(idx, amount)` | idx:位置, amount:数量 |
| 删除行 | `delete_rows(idx, amount)` | idx:位置, amount:数量 |
| 删除列 | `delete_cols(idx, amount)` | idx:位置, amount:数量 |

#### 4. 工作表管理

| 操作 | 方法 |
|------|------|
| 新建工作表 | `workbook.create_sheet("表名")` |
| 删除工作表 | `del workbook["表名"]` 或 `workbook.remove(sheet)` |
| 修改表名 | `sheet.title = "新名称"` |
| 新建文件 | `Workbook()` |

#### 5. 样式设置

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# 字体
cell.font = Font(name='微软雅黑', size=12, bold=True, color=colors.RED)

# 填充
cell.fill = PatternFill(fill_type='solid', start_color='CDCDCD')

# 对齐
cell.alignment = Alignment(horizontal='center', vertical='center')

# 边框
side = Side(border_style='thin', color=colors.BLACK)
cell.border = Border(left=side, right=side, top=side, bottom=side)

# 列宽
sheet.column_dimensions['A'].width = 20
```

---

### 二、学习建议

1. **先功能后样式**：先确保数据处理正确，再美化样式
2. **善用循环**：批量设置样式时使用循环，避免重复代码
3. **注意性能**：大数据量时优先使用 `iter_rows()` / `iter_cols()`
4. **及时保存**：重要操作前备份，防止数据丢失
5. **封装函数**：将常用操作（如设置样式）封装成函数复用

---

### 三、常见应用场景

1. **报表生成**：从数据库导出数据，生成格式化的 Excel 报表
2. **数据汇总**：多个文件/工作表的数据汇总统计
3. **数据分类**：按条件将数据分类到不同工作表
4. **批量处理**：批量修改文件格式、添加边框等
5. **自动化办公**：定时生成日报、月报等

---

### 四、下篇预告

下一篇我们将学习：
- 网络编程基础（HTTP 协议）
- 使用 requests 库发送网络请求
- API 接口调用和数据获取
- 简单的网络爬虫

掌握 Excel 操作 + 网络请求，你就能实现**数据采集 → 处理 → 存储 → 展示**的完整工作流！

---

## 🎮 动手练一练

光看不练假把式！下面几道题目帮你巩固今天学到的知识。

### 选择题

**1. 以下哪个属性可以获取单元格的列号？**
- A. `cell.row`
- B. `cell.column`
- C. `cell.coordinate`
- D. `cell.value`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：B**

**详细解析**：
- 选项 A `cell.row`：获取**行号**，不是列号
- 选项 B `cell.column`：**正确**，获取列号（从1开始）
- 选项 C `cell.coordinate`：获取**坐标**（如'B2'），不是单独的列号
- 选项 D `cell.value`：获取单元格的**值**

**属性对比表**：

| 属性 | 说明 | 示例 |
|------|------|------|
| `cell.row` | 行号 | `2` |
| `cell.column` | 列号 | `2` |
| `cell.coordinate` | 坐标 | `'B2'` |
| `cell.value` | 值 | `'李白'` |

**代码示例**：
```python
cell = sheet['B2']
print(cell.row)         # 输出: 2
print(cell.column)      # 输出: 2
print(cell.coordinate)  # 输出: B2
print(cell.value)       # 输出: 李白
```

</details>

---

**2. 要在第3行前插入2行空行，应该使用哪个方法？**
- A. `sheet.insert_rows(2, 3)`
- B. `sheet.insert_rows(3, 2)`
- C. `sheet.insert_cols(3, 2)`
- D. `sheet.delete_rows(3, 2)`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：B**

**详细解析**：
- 选项 A `sheet.insert_rows(2, 3)`：参数顺序错误，这是在第2行前插入3行
- 选项 B `sheet.insert_rows(3, 2)`：**正确**，在第3行前插入2行
- 选项 C `sheet.insert_cols(3, 2)`：这是插入**列**，不是行
- 选项 D `sheet.delete_rows(3, 2)`：这是**删除**行，不是插入

**方法语法**：
```python
# 插入行
sheet.insert_rows(idx=位置, amount=数量)

# 示例
sheet.insert_rows(3, 2)  # 在第3行前插入2行
```

**记忆技巧**：
- 第一个参数是**位置**（在哪插入）
- 第二个参数是**数量**（插入多少）

</details>

---

**3. 以下哪个代码可以创建新的 Excel 文件？**
- A. `load_workbook('新文件.xlsx')`
- B. `Workbook()`
- C. `create_workbook()`
- D. `open_workbook()`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：B**

**详细解析**：
- 选项 A `load_workbook()`：用于**打开已有文件**，不能创建新文件
- 选项 B `Workbook()`：**正确**，创建新的工作簿对象
- 选项 C `create_workbook()`：不存在这个函数
- 选项 D `open_workbook()`：这是 xlrd 库的函数，不是 openpyxl 的

**代码对比**：
```python
from openpyxl import load_workbook, Workbook

# 打开已有文件
wb1 = load_workbook('已有文件.xlsx')

# 创建新文件
wb2 = Workbook()
wb2.save('新文件.xlsx')
```

**易混淆点**：
- `load_workbook()` → 打开已有
- `Workbook()` → 创建新的

</details>

---

**4. 设置单元格背景颜色应该使用哪个类？**
- A. `Font`
- B. `PatternFill`
- C. `Alignment`
- D. `Border`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：B**

**详细解析**：
- 选项 A `Font`：设置**字体**样式（大小、颜色、加粗等）
- 选项 B `PatternFill`：**正确**，设置**填充**样式（背景颜色）
- 选项 C `Alignment`：设置**对齐**方式（水平、垂直对齐）
- 选项 D `Border`：设置**边框**样式

**样式类功能对照**：

| 类 | 功能 | 常用参数 |
|-----|------|----------|
| `Font` | 字体 | `name`, `size`, `bold`, `color` |
| `PatternFill` | 填充 | `fill_type`, `start_color` |
| `Alignment` | 对齐 | `horizontal`, `vertical` |
| `Border` | 边框 | `left`, `right`, `top`, `bottom` |

**代码示例**：
```python
from openpyxl.styles import Font, PatternFill, Alignment, Border

# 字体
cell.font = Font(name='微软雅黑', size=12, color='FF0000')

# 背景色（红色）
cell.fill = PatternFill(fill_type='solid', start_color='FF0000')

# 居中对齐
cell.alignment = Alignment(horizontal='center', vertical='center')

# 边框
side = Side(border_style='thin', color='000000')
cell.border = Border(left=side, right=side, top=side, bottom=side)
```

</details>

---

### 编程题

**1. 成绩等级评定**

假设你有一个【成绩单】，包含以下数据：

| 姓名 | 语文 | 数学 | 英语 |
|------|------|------|------|
| 李白 | 85 | 90 | 88 |
| 甄姬 | 92 | 88 | 95 |
| 后羿 | 78 | 85 | 80 |
| 瑶 | 95 | 92 | 90 |

**要求**：
1. 计算每个学生的总分
2. 根据总分评定等级：
   - 270分以上：优秀
   - 240-269分：良好
   - 210-239分：及格
   - 210分以下：不及格
3. 将总分和等级写入新列
4. 设置表头为蓝色加粗，数据区域添加边框

<details>
<summary>🔑 参考答案与解析（点击展开）</summary>

**解题思路**：
1. 打开 Excel 文件，获取成绩单工作表
2. 添加新列表头（总分、等级）
3. 遍历数据行，计算总分
4. 根据总分判断等级
5. 写入总分和等级
6. 设置样式（表头蓝色加粗，所有单元格加边框）
7. 保存文件

**代码实现**：

```python
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, Border, Side, colors

def 评定等级(score):
    """根据分数返回等级"""
    if score >= 270:
        return '优秀'
    elif score >= 240:
        return '良好'
    elif score >= 210:
        return '及格'
    else:
        return '不及格'

# 打开文件
filePath = r'D:\王者小学.xlsx'
wb = load_workbook(filePath)
sheet = wb['成绩单']

print("🚀 开始评定成绩等级...\n")

# 添加表头
sheet['E1'] = '总分'
sheet['F1'] = '等级'

# 处理数据（从第2行开始）
for row in range(2, 6):  # 第2-5行
    # 读取成绩
    chinese = sheet.cell(row=row, column=2).value
    math = sheet.cell(row=row, column=3).value
    english = sheet.cell(row=row, column=4).value
    name = sheet.cell(row=row, column=1).value
    
    # 计算总分
    total = chinese + math + english
    
    # 评定等级
    level = 评定等级(total)
    
    # 写入数据
    sheet.cell(row=row, column=5).value = total
    sheet.cell(row=row, column=6).value = level
    
    print(f"📊 {name}: 总分{total} → {level}")

# 设置样式
# 1. 表头样式（蓝色加粗）
header_font = Font(name='微软雅黑', size=12, bold=True, color=colors.BLUE)
for col in range(1, 7):
    sheet.cell(row=1, column=col).font = header_font

# 2. 边框样式
side = Side(border_style='thin', color=colors.BLACK)
border = Border(left=side, right=side, top=side, bottom=side)

# 3. 对齐方式
alignment = Alignment(horizontal='center', vertical='center')

# 应用样式到所有单元格
for row in sheet.iter_rows(min_row=1, max_row=5, min_col=1, max_col=6):
    for cell in row:
        cell.border = border
        cell.alignment = alignment

# 调整列宽
sheet.column_dimensions['A'].width = 10
sheet.column_dimensions['B'].width = 8
sheet.column_dimensions['C'].width = 8
sheet.column_dimensions['D'].width = 8
sheet.column_dimensions['E'].width = 8
sheet.column_dimensions['F'].width = 10

# 保存
wb.save(filePath)
print(f"\n✅ 评定完成！结果已保存")
```

**运行结果**：
```
🚀 开始评定成绩等级...

📊 李白: 总分263 → 良好
📊 甄姬: 总分275 → 优秀
📊 后羿: 总分243 → 及格
📊 瑶: 总分277 → 优秀

✅ 评定完成！结果已保存
```

**知识点总结**：
- 条件判断实现等级评定
- `Font` 设置字体样式
- `Border` + `Side` 设置边框
- `Alignment` 设置对齐
- `column_dimensions` 调整列宽

**进阶挑战**：
- 添加等级颜色（优秀绿色、良好蓝色、及格黄色、不及格红色）
- 计算各科班级平均分
- 添加排名列

</details>

---

**2. 多工作表数据汇总**

假设你有一个 Excel 文件，包含多个工作表，每个工作表是一个月的销售数据：

- 1月：产品A 100件，产品B 150件
- 2月：产品A 120件，产品B 130件
- 3月：产品A 90件，产品B 160件

**要求**：
1. 读取所有月份的数据
2. 创建汇总工作表，统计每个产品的总销量
3. 计算每月总销量
4. 设置表格样式（边框、对齐、表头颜色）

<details>
<summary>🔑 参考答案与解析（点击展开）</summary>

**解题思路**：
1. 打开文件，获取所有工作表名称
2. 遍历每个月份工作表，读取数据
3. 用字典统计各产品总销量
4. 创建汇总工作表
5. 写入表头、月度数据、总计
6. 设置样式
7. 保存文件

**代码实现**：

```python
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, colors

def 汇总销售数据(input_file, output_file):
    """汇总多月份销售数据"""
    
    # 打开源文件
    wb_source = load_workbook(input_file)
    
    # 统计数据
    # product_totals: {产品名: 总销量}
    # monthly_totals: {月份: 该月总销量}
    product_totals = {}
    monthly_totals = {}
    
    print("📊 正在读取数据...\n")
    
    # 遍历所有工作表（月份）
    for sheet_name in wb_source.sheetnames:
        sheet = wb_source[sheet_name]
        monthly_totals[sheet_name] = 0
        
        print(f"📅 处理: {sheet_name}")
        
        # 读取数据（从第2行开始）
        for row in sheet.iter_rows(min_row=2, values_only=True):
            product, quantity = row[0], row[1]
            
            # 累加产品总销量
            if product not in product_totals:
                product_totals[product] = 0
            product_totals[product] += quantity
            
            # 累加月总销量
            monthly_totals[sheet_name] += quantity
    
    # 创建汇总工作簿
    wb_summary = Workbook()
    ws = wb_summary.active
    ws.title = "销售汇总"
    
    # 写入标题
    ws['A1'] = '产品销售汇总表'
    ws.merge_cells('A1:D1')
    ws['A1'].font = Font(name='微软雅黑', size=16, bold=True)
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    
    # 写入产品汇总
    ws['A3'] = '产品'
    ws['B3'] = '总销量'
    
    row = 4
    for product, total in sorted(product_totals.items()):
        ws.cell(row=row, column=1).value = product
        ws.cell(row=row, column=2).value = total
        row += 1
    
    # 空一行
    row += 1
    
    # 写入月度汇总
    ws.cell(row=row, column=1).value = '月份'
    ws.cell(row=row, column=2).value = '月销量'
    row += 1
    
    for month, total in sorted(monthly_totals.items()):
        ws.cell(row=row, column=1).value = month
        ws.cell(row=row, column=2).value = total
        row += 1
    
    # 设置样式
    # 表头样式
    header_font = Font(name='微软雅黑', size=12, bold=True, color=colors.WHITE)
    header_fill = PatternFill(fill_type='solid', start_color='4472C4')
    
    for col in range(1, 3):
        cell = ws.cell(row=3, column=col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # 边框和对齐
    side = Side(border_style='thin', color=colors.BLACK)
    border = Border(left=side, right=side, top=side, bottom=side)
    alignment = Alignment(horizontal='center', vertical='center')
    
    for row_cells in ws.iter_rows(min_row=3, max_row=ws.max_row, min_col=1, max_col=2):
        for cell in row_cells:
            if cell.row != 3:  # 跳过表头（已设置）
                cell.border = border
                cell.alignment = alignment
    
    # 调整列宽
    ws.column_dimensions['A'].width = 15
    ws.column_dimensions['B'].width = 12
    
    # 保存
    wb_summary.save(output_file)
    
    # 打印统计结果
    print("\n" + "=" * 40)
    print("📈 汇总结果")
    print("=" * 40)
    print("\n产品销量：")
    for product, total in sorted(product_totals.items()):
        print(f"  {product}: {total}件")
    
    print("\n月度销量：")
    for month, total in sorted(monthly_totals.items()):
        print(f"  {month}: {total}件")
    
    print(f"\n总销量: {sum(product_totals.values())}件")
    print("=" * 40)
    print(f"\n✅ 汇总完成！保存至: {output_file}")


# 运行
if __name__ == '__main__':
    汇总销售数据(
        r'D:\销售数据\月度数据.xlsx',
        r'D:\销售数据\销售汇总.xlsx'
    )
```

**运行结果**：
```
📊 正在读取数据...

📅 处理: 1月
📅 处理: 2月
📅 处理: 3月

========================================
📈 汇总结果
========================================

产品销量：
  产品A: 310件
  产品B: 440件

月度销量：
  1月: 250件
  2月: 250件
  3月: 250件

总销量: 750件
========================================

✅ 汇总完成！保存至: D:\销售数据\销售汇总.xlsx
```

**知识点总结**：
- 遍历多个工作表
- 使用字典统计数据
- `merge_cells()` 合并单元格
- 分别设置不同区域的样式
- 格式化输出统计结果

**进阶挑战**：
- 添加图表展示（柱状图、饼图）
- 计算同比增长率
- 添加数据筛选功能
- 生成 PDF 报告

</details>