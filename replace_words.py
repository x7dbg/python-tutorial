import os
import re

base_dir = r"c:\Users\Mr.Xiao\Desktop\ziliao"

# 定义替换规则
replacements = [
    (r'本期训练营', '本教程'),
    (r'训练营', '教程'),
    (r'本课程', '本文档'),
    (r'课程总结', '文档总结'),
    (r'课程特色', '文档特色'),
    (r'课程目录', '文档目录'),
    (r'第(\d+)课', r'第\1篇'),
    (r'每节课', '每篇文档'),
    (r'这节课', '这篇文档'),
    (r'课前回顾', '内容回顾'),
    (r'课后练习', '巩固练习'),
    (r'课后习题', '练习题'),
    (r'课后作业', '作业'),
    (r'上课前', '阅读前'),
    (r'该上课了', '继续学习'),
    (r'今天的课程', '本文档'),
    (r'本节课程', '本篇文档'),
    (r'本讲', '本篇'),
]

def replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 处理所有md文件
md_files = [f for f in os.listdir(base_dir) if f.endswith('.md')]
modified_files = []

for filename in md_files:
    file_path = os.path.join(base_dir, filename)
    if replace_in_file(file_path):
        modified_files.append(filename)

print(f"已修改 {len(modified_files)} 个文件：")
for f in modified_files:
    print(f"  - {f}")