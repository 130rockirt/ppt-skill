# 配图生成 Prompt 模板库

按 SKILL.md §5 使用：调用图像生成工具时，把下面的 prompt 复制后替换主题描述即可。
所有 prompt 都已内置「配色与主题一致 + 无文字 + 高质量」约束。

---

## 通用模板

```
{主题描述}, {构图}, {配色}, {风格}, no text, no letters, no numbers, no watermark, high quality, consistent color grading
```

| 槽位 | 说明 | 示例 |
|---|---|---|
| 主题描述 | 画面主体内容 | a cheerful school campus at sunrise with students walking in |
| 构图 | 配合版式 | wide horizontal, centered subject / side composition |
| 配色 | 与页面主色阶一致 | deep teal #1F3A4E, warm amber #D97706, warm paper background |
| 风格 | 全篇统一一种 | clean flat vector illustration / minimal editorial / soft 3D render |

---

## 三式配图 prompt 示例

### 式一：左图右文（竖向或横向侧图，主体偏一侧）
```
a cheerful school campus at sunrise, a friendly school building with a clock, students with backpacks walking in, trees and soft morning light, side composition with subject on the left, deep teal #1F3A4E and warm amber #D97706 color palette, warm paper background, clean flat vector illustration, no text, no letters, no numbers, no watermark, high quality, consistent color grading
```

### 式二：上下结构（宽幅大图，主体居中）
```
a child setting a small paper sailboat with an amber sail on gentle teal waves toward a distant lighthouse, wide horizontal composition, centered subject, generous negative space above and below, deep teal #1F3A4E and warm amber #D97706 color palette, warm paper background, clean flat vector illustration, no text, no letters, no numbers, no watermark, high quality, consistent color grading
```

### 式三：左文右图（竖向或横向侧图，主体偏一侧）
```
a green sprout growing from an open book, leaves reaching toward a warm sun, small stars and hearts around, centered subject with subject on the right, deep teal #1F3A4E and warm amber #D97706 and soft green #5E8A62 color palette, warm paper background, clean flat vector illustration, no text, no letters, no numbers, no watermark, high quality, consistent color grading
```

---

## 常用主题 prompt 速查

| 主题 | prompt 片段 |
|---|---|
| 时间管理 | a clean round clock, an hourglass, an alarm clock and a calendar page floating around, organized calm feeling |
| 阅读/学习 | an open book with pages turning into flying paper birds, warm light |
| 目标/成长 | a small paper boat sailing toward a flag on a lighthouse, guiding stars |
| 习惯养成 | a sprout growing from an open book toward the sun, small star motifs |
| 团队合作 | diverse children building a bridge of building blocks together |
| 科技/创新 | geometric abstract circuit lines and glowing nodes, minimal tech style |
| 自然/环保 | rolling hills, a river, trees and a rising sun, soft morning mood |
| 节日/庆典 | festive bunting flags, confetti and warm lanterns, joyful atmosphere |

---

## 落地三步

1. 生成图默认带背景 → 用 AI 抠图（创客贴批量抠图 / remove.bg）得到透明 PNG。
2. 色调不统一 → 统一调色（同一滤镜 / 色温 / 饱和度）。
3. 文字层 → 回 PPT 用文本框叠加（黑体标题 / 宋体正文），生成图只保留纯图形区。