---
name: wordcount-check
description: Use when checking if chapter word counts meet the target (2000-2500 words). Trigger when user asks to check word count, verify chapter length, or review chapter statistics.
type: project
---

# 字数检查技能

检查《裂星衍道》各章节**正文字数**是否达标。

## 字数标准

- **目标范围**：2000-2500字
- **最低线**：2000字（不足需扩充）
- **最高线**：2500字（超出可精简）

## 统计范围

**只统计正文内容**，不包括：
- 章节标题行
- 末尾的"---"分隔符后的【本章要点】总结部分

## 使用方法

运行字数检查脚本：

```bash
cd "E:\application\book\one" && python check_target.py
```

## 检查脚本

脚本位置：`check_target.py`

核心逻辑：
```python
import os
import glob

all_files = glob.glob('第一卷（裂土求生）/**/*.txt', recursive=True)
all_files.sort(key=lambda x: int(os.path.basename(x).split('第')[1].split('章')[0]))

for f in all_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        # 去掉章节末尾的【本章要点】部分
        if '---' in content:
            body = content.split('---')[0]
        else:
            body = content
        chars = len(body.strip())

        if 2000 <= chars <= 2500:
            status = "[OK]"
        elif chars < 2000:
            status = "[少]"
        else:
            status = "[多]"

        print(f'{name}: {chars}字 {status}')
```

## 输出格式

| 章节 | 字数 | 状态 |
|------|------|------|
| 第X章 | XXXX字 | [OK]/[少]/[多] |

## 状态说明

- `[OK]`：达标（2000-2500字）
- `[少]`：偏少（<2000字，需补充）
- `[多]`：偏多（>2500字，可精简）

## 常见问题

### 字数偏少怎么办？

扩充以下内容：
1. **环境描写**：天气、光线、声音、气味
2. **心理活动**：主角思考、情感波动
3. **动作细节**：战斗或动作的详细描写
4. **对话互动**：增加角色对话

### 字数偏多怎么办？

精简以下内容：
1. 删除重复描写
2. 缩短战斗过程（保留关键动作）
3. 精简对话（保留关键信息）

## 扩充技巧示例

**环境描写扩充**：
```
原文：天气很热。
扩充：烈日炙烤着大地，空气中弥漫着干燥的热浪，连远处的山脉都笼罩在一层朦胧的尘埃中...
```

**心理活动扩充**：
```
原文：林衍很担心。
扩充：林衍的心中涌起一股不安——这高温来得太突然，太诡异。科学？天灾？还是某种更神秘的力量？他的脑海中闪过无数猜测...
```