---
name: boundary-consistency-check
description: 境界逻辑一致性检查反馈
type: feedback
---

# 境界一致性检查

## 规则

**创作任何章节或规划文档前，必须核对境界逻辑一致性：**
- 当前境界 → 下一境界是否符合九级顺序？
- 不同文档中同一节点的境界是否一致？

---

## Why：2026-04-24重大境界错误教训

发现多处文档境界设定矛盾，导致创作错误：

1. **第一卷volume1-chapters.md混乱**：第38章写"灵境初期"，第74章又写"凡境巅峰"，第76章直接跳"地境初期"——完全违背境界顺序

2. **第二卷规划错误**：写"天境后期→地境初期"为突破，实际天境后是**皇境**，不是地境

3. **多文档不一致**：outline.md、chapter-summary.md、volume2-chapters.md、writing-snapshot.md、foreshadowing-tracker.md境界描述各异

**根本原因**：混淆境界顺序，忘记"地境"在"灵境之后、天境之前"，误以为天境后是地境

---

## How to apply

**创作前检查清单**：

1. 确认当前境界（查MEMORY.md或writing-snapshot.md）
2. 确认下一境界是否正确衔接（凡→灵→地→天→皇→尊→帝→道→混沌）
3. 跨文档核对：同一章节在volume-chapters.md、outline.md、chapter-summary.md中境界是否一致
4. 若发现矛盾，立即修正所有相关文档

**纠正范围**（本次修正）：
- 章节文件（第126-128章）
- volume1-chapters.md、volume2-chapters.md
- outline.md、chapter-summary.md、writing-snapshot.md
- foreshadowing-tracker.md、characters.md
- 内存boundary-system.md

---

**更新时间**：2026-04-24