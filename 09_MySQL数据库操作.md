# 📊 数据库操作——数据的"保险箱"

## 🎯 上集回顾

上一篇我们学习了多进程与多线程编程，掌握了如何让程序"分身有术"，同时处理多个任务。进程就像独立的工厂，线程就像工厂里的工人，合理运用它们可以大幅提升程序效率。

今天，我们要学习另一个编程必备技能——**数据库操作**。如果说变量和文件是数据的"临时住所"，那么数据库就是数据的"豪华别墅"，专门用来安全、高效地存储和管理海量数据。

## 📚 数据库概述

### 🤔 为什么要使用数据库？

想象一下，你要管理一个学校的学生信息：

**方式一：文本文件存储**
```
张三,99
李四,85
王五,59
赵六,87
```
❌ 问题：格式不统一，查询困难，数据量大时内存装不下

**方式二：JSON文件存储**
```json
[
  {"name":"张三","score":99},
  {"name":"李四","score":85}
]
```
❌ 问题：虽然结构化，但仍需全部读入内存才能查询

**方式三：数据库** ⭐
```sql
SELECT name, score FROM students WHERE score > 90;
```
✅ 优势：
- 📦 **结构化存储**：数据按表组织，关系清晰
- ⚡ **快速查询**：无需加载全部数据，直接定位目标
- 🔒 **数据安全**：支持事务、备份、权限控制
- 🚀 **海量数据**：轻松处理百万、千万级数据

> 💡 **一句话总结**：数据库是专门用来**安全、高效、结构化**存储和管理数据的软件系统。

---

### 🗄️ 数据库的分类

```
┌─────────────────────────────────────────────────────────┐
│                      数据库家族                          │
├─────────────────────────┬───────────────────────────────┤
│    关系型数据库 (SQL)    │      非关系型数据库 (NoSQL)    │
├─────────────────────────┼───────────────────────────────┤
│ 📊 数据以表格形式存储     │ 📦 数据以键值对/文档/图等形式  │
│ 🔗 表与表之间有关联关系   │ 🔄 灵活的数据模型              │
│ 📝 使用 SQL 语言操作      │ 🚀 高性能、高扩展              │
├─────────────────────────┼───────────────────────────────┤
│ • MySQL                 │ • MongoDB (文档型)             │
│ • PostgreSQL            │ • Redis (键值型)               │
│ • SQLite                │ • Neo4j (图数据库)             │
│ • Oracle                │ • Cassandra (列存储)           │
│ • SQL Server            │ • Elasticsearch (搜索引擎)     │
└─────────────────────────┴───────────────────────────────┘
```

---

### 🎯 为什么选择 SQLite？

SQLite 是一个**嵌入式关系型数据库**，特点如下：

| 特性 | 说明 |
|------|------|
| 🆓 **免费开源** | 零成本，可商用 |
| 📦 **零配置** | 无需安装服务器，开箱即用 |
| 🪶 **轻量级** | 整个数据库就是一个文件 |
| 🐍 **Python内置** | 直接导入 `sqlite3` 模块即可使用 |
| 📱 **跨平台** | Windows、Mac、Linux、Android、iOS 都支持 |

> 🌰 **生活比喻**：
> - **MySQL/PostgreSQL** 像大型超市，需要专门场地（服务器），适合大规模应用
> - **SQLite** 像家里的储物柜，小巧方便，适合本地存储和小型应用

---

### 🛠️ SQLite 管理工具

虽然可以用命令行操作 SQLite，但图形化工具更直观。推荐使用 **DB Browser for SQLite**：

![Image 1](./images/chapter09_01.png)

![Image 2](./images/chapter09_02.png)

安装后界面如下，操作非常直观：

![DB Browser 主界面](https://sqlitebrowser.org/images/screenshot.png)

> 💡 **课后作业**：下载安装 DB Browser，用它打开我们代码创建的数据库文件，可视化查看数据！

---

### 📖 学习路径建议

```
┌─────────────────────────────────────────────────────────┐
│                    数据库学习路线图                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  第1步：掌握 SQL 基础                                    │
│     ├── SQLite（入门首选）✅ 当前学习                    │
│     ├── MySQL（生产环境最常用）                          │
│     └── PostgreSQL（功能强大）                           │
│         │                                               │
│         ▼                                               │
│  第2步：学习数据库设计                                    │
│     ├── 表结构设计                                       │
│     ├── 索引优化                                         │
│     └── 事务管理                                         │
│         │                                               │
│         ▼                                               │
│  第3步：了解 NoSQL（可选）                                │
│     ├── Redis（缓存）                                    │
│     ├── MongoDB（文档型）                                │
│     └── Elasticsearch（搜索）                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> 💡 **建议**：先扎实掌握 SQL 基础，再学习 NoSQL 会事半功倍！

## 🔧 Python 操作 SQLite 数据库

### 🎯 核心概念：Connection 和 Cursor

在 Python 中操作数据库，只需要记住两个核心对象：

```
┌─────────────────────────────────────────────────────────┐
│                  Python 数据库操作模型                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   🏦 Connection（连接对象）                              │
│   ├── 作用：建立与数据库的连接                            │
│   ├── 类比：就像打开保险箱的钥匙                          │
│   └── 方法：                                              │
│       ├── cursor()  - 创建游标                           │
│       ├── commit()  - 提交事务                           │
│       └── close()   - 关闭连接                           │
│            │                                            │
│            ▼                                            │
│   🎯 Cursor（游标对象）                                  │
│   ├── 作用：执行 SQL 语句，获取结果                       │
│   ├── 类比：就像保险箱里的抽屉，用来存取数据               │
│   └── 方法：                                              │
│       ├── execute()     - 执行单条 SQL                   │
│       ├── executemany() - 执行多条 SQL                   │
│       ├── fetchall()    - 获取所有结果                   │
│       └── close()       - 关闭游标                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> ⚠️ **重要提醒**：
> - `Connection` 和 `Cursor` 使用完后**必须关闭**！
> - 增删改操作后必须调用 `commit()` 提交，否则数据不会保存！
> - 建议使用 `try...except...finally` 确保资源正确释放

---

### 🚀 完整示例：创建数据库并操作数据

下面是一个完整的示例，演示如何：
1. 创建数据库文件
2. 创建数据表
3. 插入数据
4. 查询数据
5. 关闭连接

```python
# -*- coding: UTF-8 -*-
import sqlite3
import os
import json

dbPath = "data.sqlite"
# 只有data.sqlite文件不存在时才创建该文件
if not os.path.exists(dbPath):
    # 创建 SQLite数据库
    conn = sqlite3.connect(dbPath)
    # 获取 sqlite3.Cursor 对象
    cursor = conn.cursor()
    # 创建 Persons 表
    cursor.execute("""CREATE TABLE persons (
        id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        age INT NOT NULL,
        address CHAR(50),
        salary REAL
    ); """)
    # 关闭游标
    cursor.close()
    # 修改数据库后必须调用 commit 方法提交才能生效
    conn.commit()
    # 关闭数据库连接
    conn.close()
    print("创建数据库成功")

conn = sqlite3.connect(dbPath)
c = conn.cursor()
# 删除 persons 表中的所有数据
c.execute("delete from persons;")
# 下面的 4 条语句向 persons表中插入4条记录
c.execute("INSERT INTO persons(id,name,age,address,salary) VALUES(1,'张三',32,'北京',50000.00)")
c.execute("INSERT INTO persons(id,name,age,address,salary) VALUES(2,'李四',25,'上海',15000.00)")
c.execute("INSERT INTO persons(id,name,age,address,salary) VALUES(3,'王五',23,'深圳',20000.00)")
c.execute("INSERT INTO persons(id,name,age,address,salary) VALUES(4,'渣男教父',25,'长沙',60000.00)")
#  必须提交才能生效
conn.commit()  # 提交事务
print("插入数据成功")

# 查询 persons 表中的所有记录，并按age升序排列
c.execute("SELECT name,age,address,salary from persons order by age")
# 利用fetchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录
persons = c.fetchall()
print(type(persons))
for person in persons:
    print(type(person), person)

# 将查询结果转换为字符串形式，如果要将数据通过网络传输，就需要首先转换为字符串形式才能传输
resultStr = json.dumps(persons)
print(type(resultStr))
print(resultStr)
c.close()
conn.close()
```

> 💡 **代码解析**：
> - `sqlite3.connect(dbPath)` - 连接数据库（不存在则自动创建）
> - `conn.cursor()` - 创建游标对象
> - `cursor.execute(sql)` - 执行 SQL 语句
> - `conn.commit()` - **必须提交**，否则数据不会保存！
> - `cursor.fetchall()` - 获取所有查询结果
> - `cursor.close()` / `conn.close()` - **必须关闭**，释放资源

---

### 📋 SQL 速查表

SQLite 支持标准 SQL 语句，下面是常用的 **增删改查**（CRUD）操作：

| 操作 | SQL 语句 | 说明 |
|------|----------|------|
| **增** (Create) | `INSERT INTO 表名 VALUES (...)` | 插入新数据 |
| **删** (Delete) | `DELETE FROM 表名 WHERE 条件` | 删除数据 |
| **改** (Update) | `UPDATE 表名 SET 列=值 WHERE 条件` | 修改数据 |
| **查** (Retrieve) | `SELECT 列名 FROM 表名 WHERE 条件` | 查询数据 |

---

## 🔍 查询数据 SELECT

### 1️⃣ 查询所有记录

```sql
SELECT * FROM persons ORDER BY age DESC;
```

- `*` - 查询所有列
- `ORDER BY age` - 按 age 列排序（默认升序 ASC）
- `DESC` - 降序排列（从大到小）

**代码示例**：

```python
# 导入sqlite3模块
from sqlite3 import Error
import sqlite3

# try-except:防止因连接失败导致程序崩溃
try:
    # 数据库文件路径
    db_file = 'data.sqlite'
    # 连接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    cour = conn.cursor()
    # 查询语句sql：select 列名(*-所有列) from 表名 [where 条件] [order by 列名]
    sql = 'select * from persons order by age desc'
    # 执行sql语句
    cour.execute(sql)
    # 打印查询结果
    print(cour.fetchall())
    # 关闭游标
    cour.close()
    # 关闭连接
    conn.close()
except Error as e:
    print('连接失败')
```

---

### 2️⃣ 条件查询

使用 `WHERE` 子句添加查询条件：

```sql
SELECT * FROM persons WHERE name = '张三';
```

**⚠️ 安全提示：使用 `?` 占位符防止 SQL 注入！**

```python
# ❌ 错误写法（有 SQL 注入风险）
sql = f"SELECT * FROM persons WHERE name = '{user_input}'"

# ✅ 正确写法（使用占位符）
sql = "SELECT * FROM persons WHERE name = ?"
cursor.execute(sql, ('张三',))  # 参数必须是元组
```

> 🛡️ **什么是 SQL 注入？**
> 
> 如果用户输入 `' OR '1'='1`，错误写法会变成：
> ```sql
> SELECT * FROM persons WHERE name = '' OR '1'='1'
> ```
> 这将返回所有记录！使用 `?` 占位符可以避免这种攻击。

```python
# 导入sqlite3模块
from sqlite3 import Error
import sqlite3

# try-except:防止因连接失败导致程序崩溃
try:
    # 数据库文件路径
    db_file = 'data.sqlite'
    # 连接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    cour = conn.cursor()
    # 编写sql语句
    # 查询语句sql：select 列名(*-所有列) from 表名 [where 条件]
    # ?-占位符，在cour.execute()参数中，传入数据元组
    sql = 'select * from persons where name=?'
    # 构建数据元组
    name = ('渣男教父',)
    # 执行sql语句
    cour.execute(sql, name)
    # 打印查询结果
    print(cour.fetchall())
    # 关闭游标
    cour.close()
    # 关闭连接
    conn.close()
except Error as e:
    print('连接失败')

cursor.execute('SELECT name,age,address,salary from persons where name=?', ('渣男教父',))

---

## ➕ 增加数据 INSERT

### 1️⃣ 插入单条记录

```sql
INSERT INTO persons(id, name, age, address, salary) 
VALUES (5, '托尼老弟', 35, '长沙', 6000.00);
```

**代码示例**：

```python
# 导入sqlite3模块
from sqlite3 import Error
import sqlite3

# try-except:防止因连接失败导致程序崩溃
try:
    # 数据库文件路径
    db_file = 'data.sqlite'
    # 连接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    cour = conn.cursor()
    # 编写sql语句
    # 添加语句sql：INSERT INTO 表名(列名)
    # VALUES (<列1的值>,[<列2的值>,<列3的值>]);
    # ?-占位符，在cour.execute()参数中，传入数据元组
    # 主键id也可设置为自增，自增的列可以不需要传入
    sql = 'INSERT INTO persons(id,name,age,address,salary) VALUES(?,?,?,?,?)'
    # 构建数据元组
    p_data = (5, '托尼老弟', 35, '长沙', 6000.00)
    # 执行sql语句
    cour.execute(sql, p_data)
    # 提交数据-同步到数据库文件-增删改查，除了查询以外有需要进行提交
    conn.commit()
    # 打印受影响的行数
    print(cour.rowcount)
    # 关闭游标
    cour.close()
    # 关闭连接
    conn.close()
except Error as e:
    print('连接失败')
```

---

### 2️⃣ 插入多条记录

使用 `executemany()` 方法批量插入：

```python
# 导入sqlite3模块
from sqlite3 import Error
import sqlite3

# try-except:防止因连接失败导致程序崩溃
try:
    # 数据库文件路径
    db_file = 'data.sqlite'
    # 连接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    cour = conn.cursor()
    # 编写sql语句
    # 添加语句sql：INSERT INTO 表名(列名)
    # VALUES (<列1的值>,[<列2的值>,<列3的值>]);
    # ?-占位符，在cour.execute()参数中，传入数据元组
    sql = 'INSERT INTO persons(id,name,age,address,salary) VALUES(?,?,?,?,?)'
    # 构建数据元组列表
    p_data = [
        (6, '张三', 32, '北京', 50000.00),
        (7, '李四', 25, '上海', 15000.00),
        (8, '王五', 23, '深圳', 20000.00)
    ]
    # 执行sql语句
    cour.executemany(sql, p_data)
    # 提交数据-同步到数据库文件-增删改查，除了查询以外有需要进行提交
    conn.commit()
    # 打印受影响的行数
    print(cour.rowcount)
    # 关闭游标
    cour.close()
    # 关闭连接
    conn.close()
except Error as e:
    print('连接失败')
```

---

## ✏️ 修改数据 UPDATE

### 修改记录

```sql
UPDATE persons SET salary = 106000 WHERE name = '渣男教父';
```

**⚠️ 注意：不要忘记 `WHERE` 子句！**

```sql
-- ❌ 危险！会修改所有记录的 salary
UPDATE persons SET salary = 106000;

-- ✅ 正确！只修改 name='渣男教父' 的记录
UPDATE persons SET salary = 106000 WHERE name = '渣男教父';
```

```python
# 导入sqlite3模块
from sqlite3 import Error
import sqlite3

# try-except:防止因连接失败导致程序崩溃
try:
    # 数据库文件路径
    db_file = 'data.sqlite'
    # 连接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    cour = conn.cursor()
    # 编写sql语句
    # 修改语句sql：UPDATE  <表名>
    # SET  <列名1>=<值1>[,<列名2>=<值2>]
    # [WHERE <条件>];
    # ?-占位符，在cour.execute()参数中，传入数据元组
    sql = 'update persons set salary=? where name=?'
    # 构建数据元组
    p_data = (106000, '渣男教父')
    # 执行sql语句
    cour.execute(sql, p_data)
    # 提交数据-同步到数据库文件-增删改查，除了查询以外有需要进行提交
    conn.commit()
    # 打印受影响的行数
    print(cour.rowcount)
    # 关闭游标
    cour.close()
    # 关闭连接
    conn.close()
except Error as e:
    print('连接失败')
```

---

## 🗑️ 删除数据 DELETE

### 1️⃣ 删除单条记录

```sql
DELETE FROM persons WHERE id = 1;
```

**⚠️ 注意：`DELETE` 也需要 `WHERE` 子句！**

```sql
-- ❌ 危险！会删除所有记录
DELETE FROM persons;

-- ✅ 正确！只删除 id=1 的记录
DELETE FROM persons WHERE id = 1;
```

```python
# 导入sqlite3模块
from sqlite3 import Error
import sqlite3

# try-except:防止因连接失败导致程序崩溃
try:
    # 数据库文件路径
    db_file = 'data.sqlite'
    # 连接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    cour = conn.cursor()
    # 编写sql语句
    # 删除语句sql：DELETE FROM 表名
    # WHERE <列名1>=<值1>
    # ?-占位符，在cour.execute()参数中，传入数据元组
    sql = 'delete from persons where id=?'
    # 构建数据元组
    p_data = (1,)
    # 执行sql语句
    cour.execute(sql, p_data)
    # 提交数据-同步到数据库文件-增删改查，除了查询以外有需要进行提交
    conn.commit()
    # 打印受影响的行数
    print(cour.rowcount)
    # 关闭游标
    cour.close()
    # 关闭连接
    conn.close()
except Error as e:
    print('连接失败')
```

---

### 2️⃣ 删除多条记录

同样使用 `executemany()` 批量删除：

```python
# 导入sqlite3模块
from sqlite3 import Error
import sqlite3

# try-except:防止因连接失败导致程序崩溃
try:
    # 数据库文件路径
    db_file = 'data.sqlite'
    # 连接数据库
    conn = sqlite3.connect(db_file)
    # 创建游标
    cour = conn.cursor()
    # 编写sql语句
    # 删除语句sql：DELETE FROM 表名
    # WHERE <列名1>=<值1>
    # ?-占位符，在cour.execute()参数中，传入数据元组
    sql = 'delete from persons where id=?'
    # 构建数据元组列表
    p_data = [(2,), (3,)]
    # 执行sql语句
    cour.executemany(sql, p_data)
    # 提交数据-同步到数据库文件-增删改查，除了查询以外有需要进行提交
    conn.commit()
    # 打印受影响的行数
    print(cour.rowcount)
    # 关闭游标
    cour.close()
    # 关闭连接
    conn.close()
except Error as e:
    print('连接失败')
```

---

## ⚠️ 操作数据库注意事项

### 🎯 黄金法则

```
┌─────────────────────────────────────────────────────────┐
│                   数据库操作三步曲                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1️⃣ 连接数据库                                          │
│     conn = sqlite3.connect('数据库文件.db')              │
│     cursor = conn.cursor()                              │
│         │                                               │
│         ▼                                               │
│  2️⃣ 执行操作                                            │
│     cursor.execute('SQL语句')                           │
│     conn.commit()  # 增删改必须提交！                    │
│         │                                               │
│         ▼                                               │
│  3️⃣ 关闭连接                                            │
│     cursor.close()                                      │
│     conn.close()                                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 🛡️ 使用 try-except-finally 确保资源释放

```python
import sqlite3
from sqlite3 import Error

def safe_db_operation():
    """安全的数据库操作示例"""
    conn = None
    cursor = None
    
    try:
        # 1. 连接数据库
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        
        # 2. 执行 SQL
        cursor.execute("INSERT INTO users (name) VALUES (?)", ('张三',))
        conn.commit()
        
        print("✅ 操作成功！")
        
    except Error as e:
        print(f"❌ 数据库错误: {e}")
        # 发生错误时回滚事务
        if conn:
            conn.rollback()
            
    finally:
        # 3. 确保资源被释放（无论是否出错）
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("🔒 资源已释放")

# 更简洁的写法：使用上下文管理器
import contextlib

with contextlib.closing(sqlite3.connect('data.db')) as conn:
    with contextlib.closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
    # 连接会自动关闭
```

### 📋 常见错误速查表

| 错误现象 | 可能原因 | 解决方案 |
|----------|----------|----------|
| `OperationalError: no such table` | 表不存在 | 先执行 CREATE TABLE 创建表 |
| `IntegrityError: UNIQUE constraint failed` | 主键重复 | 检查插入的数据是否已存在 |
| `ProgrammingError: Incorrect number of bindings` | 参数数量不匹配 | 检查 `?` 占位符和参数元组 |
| 数据插入后查询不到 | 忘记 `commit()` | 增删改操作后必须调用 `commit()` |
| 程序运行变慢 | 连接未关闭 | 确保调用 `close()` 或使用 `with` 语句 |

## 📝 文档总结

### 一、核心知识点回顾

#### 1. 为什么要使用数据库？

| 存储方式 | 优点 | 缺点 |
|----------|------|------|
| **变量** | 访问速度快 | 程序结束数据丢失 |
| **文本文件** | 简单易用 | 查询困难，格式不统一 |
| **JSON文件** | 结构化存储 | 需全部读入内存 |
| **数据库** ⭐ | 结构化、快速查询、海量数据 | 需要学习 SQL |

#### 2. SQLite 特点

- 🆓 **免费开源** - 零成本使用
- 📦 **零配置** - 开箱即用，无需安装服务器
- 🪶 **轻量级** - 单文件数据库
- 🐍 **Python内置** - 直接导入 `sqlite3` 模块
- 📱 **跨平台** - 支持所有主流操作系统

#### 3. Python 操作数据库核心 API

```python
import sqlite3

# 1. 连接数据库（不存在则自动创建）
conn = sqlite3.connect('database.db')

# 2. 创建游标
cursor = conn.cursor()

# 3. 执行 SQL
cursor.execute("SELECT * FROM table_name")
results = cursor.fetchall()  # 获取所有结果

# 4. 增删改操作后必须提交！
conn.commit()

# 5. 关闭资源
cursor.close()
conn.close()
```

#### 4. SQL 增删改查（CRUD）

| 操作 | SQL 语句 | Python 方法 |
|------|----------|-------------|
| **增** (Create) | `INSERT INTO ... VALUES (...)` | `cursor.execute(sql, params)` |
| **删** (Delete) | `DELETE FROM ... WHERE ...` | `cursor.execute(sql, params)` |
| **改** (Update) | `UPDATE ... SET ... WHERE ...` | `cursor.execute(sql, params)` |
| **查** (Retrieve) | `SELECT ... FROM ... WHERE ...` | `cursor.execute(sql)` + `fetchall()` |
| **批量操作** | - | `cursor.executemany(sql, params_list)` |

#### 5. 安全最佳实践

```python
# ✅ 正确：使用 ? 占位符（防止 SQL 注入）
cursor.execute("SELECT * FROM users WHERE name = ?", ('张三',))

# ❌ 错误：字符串拼接（有 SQL 注入风险）
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
```

#### 6. 资源管理

```python
# 方式一：try-except-finally
try:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    # ... 操作数据库
    conn.commit()
except Error as e:
    print(f"错误: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()

# 方式二：使用上下文管理器（推荐）
import contextlib

with contextlib.closing(sqlite3.connect('db.db')) as conn:
    with contextlib.closing(conn.cursor()) as cursor:
        # ... 操作数据库
        pass
    # 自动关闭
```

---

### 二、学习路径建议

```
当前阶段 ──→ SQLite 入门（已完成）
    │
    ├──→ MySQL/PostgreSQL（生产环境数据库）
    │
    ├──→ SQL 进阶（索引、事务、优化）
    │
    └──→ ORM 框架（SQLAlchemy、Django ORM）
```

---

### 三、下篇预告

下一篇我们将学习：
- 网络编程基础（Socket编程）
- HTTP协议与Web开发
- 使用 requests 库进行网络请求

掌握数据库操作后，配合网络编程，你就可以开发完整的数据驱动型应用了！

## 🎮 动手练一练

光看不练假把式！下面几道题目帮你巩固今天学到的数据库知识。

### 选择题

**1. 数据库中有一个 `student` 表，需要查询所有学生的信息并按成绩从高到低排列，正确的 SQL 语句是？**
- A. `SELECT score FROM student`
- B. `SELECT * FROM student`
- C. `SELECT * FROM student ORDER BY score DESC`
- D. `SELECT * FROM student ORDER BY score`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：C**

**详细解析**：
- 选项 A 错误：只查询了 `score` 列，没有查询所有学生信息。
- 选项 B 错误：虽然查询了所有列，但没有排序，结果是乱序的。
- 选项 C **正确**：`SELECT *` 查询所有列，`ORDER BY score DESC` 按成绩降序排列（从高到低）。
- 选项 D 错误：`ORDER BY score` 默认是升序（ASC），结果是从低到高排列。

**关键知识点**：
```sql
-- 升序排列（默认）
SELECT * FROM student ORDER BY score;      -- 或 ORDER BY score ASC

-- 降序排列
SELECT * FROM student ORDER BY score DESC; -- 从高到低
```

**记忆技巧**：
- `ASC` = Ascending（上升）→ 从小到大
- `DESC` = Descending（下降）→ 从大到小

</details>

---

**2. 修改数据库中的数据应该使用哪个 SQL 语句？**
- A. SELECT
- B. INSERT
- C. UPDATE
- D. DELETE

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：C**

**详细解析**：
- 选项 A `SELECT`：用于**查询**数据，不会修改数据。
- 选项 B `INSERT`：用于**插入**新数据，不是修改已有数据。
- 选项 C `UPDATE`：**正确**，专门用于修改（更新）已有数据。
- 选项 D `DELETE`：用于**删除**数据，不是修改。

**CRUD 对应关系**：
| 操作 | SQL 关键字 | 含义 |
|------|-----------|------|
| Create（增） | INSERT | 插入新数据 |
| Read（查） | SELECT | 查询数据 |
| Update（改） | UPDATE | 修改数据 |
| Delete（删） | DELETE | 删除数据 |

**示例**：
```sql
-- 修改张三的成绩为 100 分
UPDATE student SET score = 100 WHERE name = '张三';
```

</details>

---

**3. 要查询 `persons` 表中"张三"的工资，以下哪个 Python 语句是正确的？**
- A. `cursor.execute('SELECT salary FROM persons WHERE name=?', ('渣男教父',))`
- B. `cursor.execute('SELECT salary FROM persons WHERE name=?', ('张三'))`
- C. `cursor.execute('SELECT salary FROM persons WHERE id=?', ('张三',))`
- D. `cursor.execute('SELECT salary FROM persons WHERE name=?', ('张三',))`

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：D**

**详细解析**：
- 选项 A 错误：查询的是 `'渣男教父'`，不是 `'张三'`。
- 选项 B 错误：参数 `'张三'` 不是元组，缺少逗号！应该是 `('张三',)`。
- 选项 C 错误：`id` 是整数类型，不应该传入字符串 `'张三'`。
- 选项 D **正确**：使用 `name=?` 作为条件，参数是元组 `('张三',)`。

**关键知识点**：
```python
# ✅ 正确：参数必须是元组，单个元素要加逗号
cursor.execute("SELECT * FROM users WHERE name = ?", ('张三',))

# ❌ 错误：不是元组
cursor.execute("SELECT * FROM users WHERE name = ?", ('张三'))

# ❌ 错误：直接传字符串
cursor.execute("SELECT * FROM users WHERE name = ?", '张三')
```

**易错点**：`('张三',)` 和 `('张三')` 完全不同！
- `('张三',)` → 元组，包含一个元素
- `('张三')` → 只是带括号的字符串，等于 `'张三'`

</details>

---

**4. 关于 Python 的 DB-API，以下说法不正确的是？**
- A. 使用 Cursor 执行 SELECT 语句时，通过 `fetchall()` 可以拿到结果集。结果集是一个 list，每个元素都是一个 tuple。
- B. 使用 Cursor 执行 INSERT、UPDATE、DELETE 语句时，通过 `rowcount` 可以获取影响的行数。
- C. 使用 Connection 和 Cursor 对象后，可以不用关闭。
- D. 使用 Connection 和 Cursor 对象后，必须进行关闭。

<details>
<summary>💡 答案解析（点击展开）</summary>

**正确答案：C**

**详细解析**：
- 选项 A 正确：`fetchall()` 返回列表，每个元素是元组，对应一行记录。
  ```python
  results = cursor.fetchall()
  # 结果：[('张三', 20), ('李四', 25)]
  ```
- 选项 B 正确：`rowcount` 返回受影响的行数。
  ```python
  cursor.execute("UPDATE users SET age = 30 WHERE name = '张三'")
  print(cursor.rowcount)  # 输出：1（影响1行）
  ```
- 选项 C **不正确**：Connection 和 Cursor 必须关闭，否则会造成**资源泄露**！
- 选项 D 正确：这是良好的编程习惯，确保资源释放。

**资源不关闭的后果**：
- 数据库连接数耗尽，无法建立新连接
- 内存占用不断增加
- 程序运行变慢甚至崩溃

**正确做法**：
```python
# 方式一：显式关闭
cursor.close()
conn.close()

# 方式二：使用 try-finally
try:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    # ... 操作
finally:
    cursor.close()
    conn.close()
```

</details>

---

### 编程题

**1. 学生成绩管理系统**

有学生成绩数据如下：

| 学号 | 姓名 | 语文 | 数学 | 英语 | 总分 |
|------|------|------|------|------|------|
| 1 | 张三 | 96 | 96 | 98 | 0 |
| 2 | 李四 | 94 | 95 | 90 | 0 |
| 3 | 王五 | 90 | 92 | 95 | 0 |
| 4 | 渣男教父 | 97 | 100 | 96 | 0 |

**要求**：
1. 创建 `students.sqlite` 数据库
2. 创建 `students` 表，包含：id（INT，主键）、name（TEXT）、chn（INT）、math（INT）、eng（INT）、total（INT）
3. 插入上述 4 行数据
4. 更新所有人的 `total` = `chn` + `math` + `eng`
5. 查询并显示所有学生信息（按总分降序排列）

**预期结果**：

![Image 3](./images/chapter09_03.png)

<details>
<summary>🔑 参考答案与解析（点击展开）</summary>

**解题思路**：
1. 连接数据库（不存在则自动创建）
2. 创建游标，执行 CREATE TABLE 创建表
3. 使用 `executemany()` 批量插入数据
4. 使用 `UPDATE` 语句计算总分
5. 使用 `SELECT` 查询并显示结果
6. 提交事务并关闭连接

**代码实现**：

```python
import sqlite3
import os

# 数据库文件路径
db_path = 'students.sqlite'

# 如果数据库已存在，先删除（方便重复运行）
if os.path.exists(db_path):
    os.remove(db_path)

# 1. 连接数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("🚀 开始创建学生成绩管理系统...\n")

# 2. 创建 students 表
cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        chn INTEGER,
        math INTEGER,
        eng INTEGER,
        total INTEGER DEFAULT 0
    )
''')
print("✅ 表创建成功！")

# 3. 插入数据
students_data = [
    (1, '张三', 96, 96, 98, 0),
    (2, '李四', 94, 95, 90, 0),
    (3, '王五', 90, 92, 95, 0),
    (4, '渣男教父', 97, 100, 96, 0)
]

cursor.executemany(
    'INSERT INTO students (id, name, chn, math, eng, total) VALUES (?, ?, ?, ?, ?, ?)',
    students_data
)
print(f"✅ 插入了 {cursor.rowcount} 条学生记录！")

# 4. 更新总分
cursor.execute('''
    UPDATE students 
    SET total = chn + math + eng
''')
print(f"✅ 更新了 {cursor.rowcount} 条记录的总分！")

# 提交事务
conn.commit()

# 5. 查询并显示结果（按总分降序）
print("\n" + "=" * 60)
print("📊 学生成绩表（按总分降序）")
print("=" * 60)
print(f"{'学号':<6}{'姓名':<12}{'语文':<8}{'数学':<8}{'英语':<8}{'总分':<8}")
print("-" * 60)

cursor.execute('SELECT * FROM students ORDER BY total DESC')
for row in cursor.fetchall():
    id, name, chn, math, eng, total = row
    print(f"{id:<6}{name:<12}{chn:<8}{math:<8}{eng:<8}{total:<8}")

print("=" * 60)

# 统计信息
cursor.execute('SELECT AVG(total), MAX(total), MIN(total) FROM students')
avg, max_score, min_score = cursor.fetchone()
print(f"\n📈 统计信息：")
print(f"   平均分：{avg:.2f}")
print(f"   最高分：{max_score}")
print(f"   最低分：{min_score}")

# 6. 关闭连接
cursor.close()
conn.close()

print("\n✅ 操作完成，数据库已保存！")
```

**运行结果**：
```
🚀 开始创建学生成绩管理系统...

✅ 表创建成功！
✅ 插入了 4 条学生记录！
✅ 更新了 4 条记录的总分！

============================================================
📊 学生成绩表（按总分降序）
============================================================
学号  姓名        语文    数学    英语    总分    
------------------------------------------------------------
4     渣男教父    97      100     96      293     
1     张三        96      96      98      290     
2     李四        94      95      90      279     
3     王五        90      92      95      277     
============================================================

📈 统计信息：
   平均分：284.75
   最高分：293
   最低分：277

✅ 操作完成，数据库已保存！
```

**知识点总结**：
- `CREATE TABLE` 创建表结构
- `executemany()` 批量插入数据
- `UPDATE` 修改数据
- `ORDER BY total DESC` 降序排列
- `AVG()`、`MAX()`、`MIN()` 聚合函数

**进阶挑战**：
- 添加异常处理（try-except）
- 实现添加/删除学生功能
- 将代码封装成类（StudentManager）
- 使用 DB Browser 打开数据库查看

</details>

---

**2. 简易图书管理系统**

**要求**：
1. 创建 `library.sqlite` 数据库
2. 创建 `books` 表，包含：
   - id（INTEGER，主键，自增）
   - title（TEXT，书名）
   - author（TEXT，作者）
   - price（REAL，价格）
   - stock（INTEGER，库存）
3. 实现以下功能函数：
   - `add_book(title, author, price, stock)` - 添加图书
   - `query_all_books()` - 查询所有图书
   - `query_by_author(author)` - 按作者查询
   - `update_stock(id, new_stock)` - 更新库存
   - `delete_book(id)` - 删除图书

<details>
<summary>🔑 参考答案与解析（点击展开）</summary>

**解题思路**：
1. 封装数据库操作到类中
2. 每个方法负责一个功能
3. 使用 `try-finally` 确保资源释放
4. 添加友好的命令行界面

**代码实现**：

```python
import sqlite3
from sqlite3 import Error
import os


class LibraryManager:
    """图书管理系统"""
    
    def __init__(self, db_file='library.sqlite'):
        """初始化，连接数据库"""
        self.db_file = db_file
        self.init_database()
    
    def get_connection(self):
        """获取数据库连接"""
        try:
            return sqlite3.connect(self.db_file)
        except Error as e:
            print(f"❌ 数据库连接失败: {e}")
            return None
    
    def init_database(self):
        """初始化数据库，创建表"""
        conn = self.get_connection()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    price REAL,
                    stock INTEGER DEFAULT 0
                )
            ''')
            conn.commit()
            print("✅ 数据库初始化成功！")
        except Error as e:
            print(f"❌ 初始化失败: {e}")
        finally:
            if conn:
                conn.close()
    
    def add_book(self, title, author, price, stock):
        """添加图书"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO books (title, author, price, stock)
                VALUES (?, ?, ?, ?)
            ''', (title, author, price, stock))
            conn.commit()
            print(f"✅ 图书《{title}》添加成功！ID: {cursor.lastrowid}")
            return True
        except Error as e:
            print(f"❌ 添加失败: {e}")
            return False
        finally:
            conn.close()
    
    def query_all_books(self):
        """查询所有图书"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books ORDER BY id')
            return cursor.fetchall()
        except Error as e:
            print(f"❌ 查询失败: {e}")
            return []
        finally:
            conn.close()
    
    def query_by_author(self, author):
        """按作者查询"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM books WHERE author = ?',
                (author,)
            )
            return cursor.fetchall()
        except Error as e:
            print(f"❌ 查询失败: {e}")
            return []
        finally:
            conn.close()
    
    def update_stock(self, book_id, new_stock):
        """更新库存"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                'UPDATE books SET stock = ? WHERE id = ?',
                (new_stock, book_id)
            )
            conn.commit()
            if cursor.rowcount > 0:
                print(f"✅ 图书 ID {book_id} 库存更新为 {new_stock}")
                return True
            else:
                print(f"⚠️ 未找到 ID 为 {book_id} 的图书")
                return False
        except Error as e:
            print(f"❌ 更新失败: {e}")
            return False
        finally:
            conn.close()
    
    def delete_book(self, book_id):
        """删除图书"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"✅ 图书 ID {book_id} 已删除")
                return True
            else:
                print(f"⚠️ 未找到 ID 为 {book_id} 的图书")
                return False
        except Error as e:
            print(f"❌ 删除失败: {e}")
            return False
        finally:
            conn.close()
    
    def display_books(self, books):
        """显示图书列表"""
        if not books:
            print("📭 暂无图书")
            return
        
        print("\n" + "=" * 80)
        print(f"{'ID':<6}{'书名':<30}{'作者':<15}{'价格':<10}{'库存':<10}")
        print("-" * 80)
        for book in books:
            id, title, author, price, stock = book
            print(f"{id:<6}{title:<30}{author:<15}¥{price:<9.2f}{stock:<10}")
        print("=" * 80)


def main():
    """主函数 - 命令行界面"""
    # 如果存在旧数据库，先删除
    if os.path.exists('library.sqlite'):
        os.remove('library.sqlite')
    
    library = LibraryManager()
    
    # 添加一些示例数据
    print("\n📚 添加示例图书...")
    library.add_book("Python编程：从入门到实践", "埃里克·马瑟斯", 89.00, 100)
    library.add_book("流畅的Python", "卢西亚诺·拉马略", 139.00, 50)
    library.add_book("Python Cookbook", "大卫·比斯利", 108.00, 80)
    library.add_book("深入理解计算机系统", "兰德尔·布莱恩特", 189.00, 30)
    
    # 显示所有图书
    print("\n📖 所有图书列表：")
    books = library.query_all_books()
    library.display_books(books)
    
    # 按作者查询
    print("\n🔍 查询作者 '埃里克·马瑟斯' 的图书：")
    books = library.query_by_author("埃里克·马瑟斯")
    library.display_books(books)
    
    # 更新库存
    print("\n📝 更新库存...")
    library.update_stock(1, 95)
    
    # 删除图书
    print("\n🗑️ 删除图书...")
    library.delete_book(4)
    
    # 显示更新后的列表
    print("\n📖 更新后的图书列表：")
    books = library.query_all_books()
    library.display_books(books)


if __name__ == '__main__':
    main()
```

**运行结果**：
```
✅ 数据库初始化成功！

📚 添加示例图书...
✅ 图书《Python编程：从入门到实践》添加成功！ID: 1
✅ 图书《流畅的Python》添加成功！ID: 2
✅ 图书《Python Cookbook》添加成功！ID: 3
✅ 图书《深入理解计算机系统》添加成功！ID: 4

📖 所有图书列表：

================================================================================
ID    书名                          作者           价格        库存      
--------------------------------------------------------------------------------
1     Python编程：从入门到实践       埃里克·马瑟斯   ¥89.00     100       
2     流畅的Python                  卢西亚诺·拉马略 ¥139.00    50        
3     Python Cookbook               大卫·比斯利     ¥108.00    80        
4     深入理解计算机系统             兰德尔·布莱恩特 ¥189.00    30        
================================================================================

🔍 查询作者 '埃里克·马瑟斯' 的图书：

================================================================================
ID    书名                          作者           价格        库存      
--------------------------------------------------------------------------------
1     Python编程：从入门到实践       埃里克·马瑟斯   ¥89.00     100       
================================================================================

📝 更新库存...
✅ 图书 ID 1 库存更新为 95

🗑️ 删除图书...
✅ 图书 ID 4 已删除

📖 更新后的图书列表：
...
```

**知识点总结**：
- 面向对象封装数据库操作
- `AUTOINCREMENT` 自增主键
- `cursor.lastrowid` 获取刚插入的记录ID
- `rowcount` 获取影响的行数
- 异常处理确保资源释放

**进阶挑战**：
- 添加图书搜索功能（按书名模糊查询）
- 实现借阅功能（记录借出/归还）
- 添加数据验证（价格必须大于0）
- 使用图形界面（tkinter）

</details>