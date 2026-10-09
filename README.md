<!-- SERIES:START -->
> **属于 [Chinese Thinkers as Skills 系列](https://github.com/constantin2088/chinese-thinkers-skills)** · [完整作品目录](https://github.com/constantin2088/chinese-thinkers-skills#作品目录)

**相关推荐**：[梁启超·自新与变局](https://github.com/constantin2088/liang-qichao-skill)

> 系列入口与推荐由总仓库 catalog/skills.json 生成。
<!-- SERIES:END -->

# 叶茂中·冲突营销 Skill

**从消费冲突到产品解决，再到可检验的表达。** 适用于卖点模糊、品牌同质化、营销转化差的中文 Agent 任务。

独立开源的现代方法转译，未获叶茂中本人、家属或相关机构授权；不模拟人物背书，不保证增长效果。

## 30 秒看效果

> 我们做上班族便利餐，想强调“健康”，但顾客嫌贵。预算 3,000 元，怎么改？

先把“嫌贵”拆成售价、饱腹、口味、等待与信任的不同解释。候选冲突：想省午休时间，却担心便捷餐不合口味；想看懂配料，却不愿为抽象“健康”溢价。对比现有替代和真实产品能力后，只对已证实的可看配料、准时取餐等优势写表达。用相同渠道、价格和随机分流的对照测试支付转化，同时监控退款与履约；没样本时不宣布成功。

→ [完整演示和实验表](examples/meal.md)。这里的预算与情境为教学假设，未执行投放。

## 工作流

购买情境 → 候选冲突 → 消费者／竞争／自身三方检查 → 产品解决 → 有证据的表达 → 对照实验与反证。

从叶茂中署名的[《冲突是营销的魂》](https://www.jjckb.cn/2017-08/29/c_136564522.htm)提取需求洞察与三方检查线索；证据表、淘汰门槛和实验设计均是本项目的现代实现。详见 [来源](references/sources.md) 和 [方法分层](references/frameworks.md)。

## 安装和使用

本项目与梁启超 Skill 一样，直接通过公开仓库发布，不使用 GitHub Releases。

```bash
npx skills add constantin2088/ye-maozhong-skill
```

也可把仓库完整复制到客户端支持的 skills 目录，保留 SKILL.md 与 references。具体发现路径依客户端文档；本次未声称所有客户端安装均已验证。

示例请求：

- 用冲突营销分析这个产品。把消费者证据与我们的猜测分开，别先写口号。
- 对这三条卖点做消费者、竞争替代、产品能力三方筛选。
- 为我们的新表达设计小预算对照实验，给出停止条件。

## 示例与反例

| 情境 | 核心判断 | 完整案例 |
|---|---|---|
| 便利餐 | 抽象健康口号需要具体购买证据 | [meal](examples/meal.md) |
| B2B 软件 | 少做报表与责任可追溯要同时解决 | [b2b](examples/b2b.md) |
| 质量投诉 | 产品兑现失败先整改，再考虑传播 | [failure](examples/failure.md) |

这些为项目原创虚构演示，不是叶茂中客户案例或已验证商业成果。

## 验证与发布

```bash
python scripts/check_skill.py . --release
python -m unittest discover -s tests -v
```

结构检查和实验计算有自动测试；可运行 `python scripts/experiment_metrics.py 10 100 15 100` 查看小样本差值及不确定区间。模型回答的语义质量另按 [行为评测](evals/test-cases.md) 人工评分。不能把文件校验通过当成模型评测通过。执行记录见 [评测记录](evals/results.md)。

贡献需补来源、边界、示例和回归用例。发布步骤见 [PUBLISHING.md](PUBLISHING.md)，版权归属见 [NOTICE.md](NOTICE.md)。MIT 仅覆盖本项目原创内容。
