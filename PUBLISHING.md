# 发布规范

1. 新事实或引语补 sources.md 的版本、定位、核查日期；方法变化同步 examples 与 evals。
2. 执行 `python scripts/check_skill.py . --release`、`python -m unittest discover -s tests -v` 和 `python scripts/check_links.py`。
3. 按 evals/test-cases.md 记录独立模型回答。未执行必须在 evals/results.md 中披露，不能声称行为测试通过。
4. 从总目录刷新系列区块：`python scripts/sync_series.py --slug ye-maozhong-skill`。
5. 用已有管理权限同步 About：`python scripts/sync_series.py --slug ye-maozhong-skill --metadata --apply`。先不带 --apply 可预览。
6. 审查差异，提交到 main 后确认对应 SHA 的 GitHub CI 全绿，即完成 Skill 发布。与梁启超仓库保持一致，不创建 GitHub Releases；安装直接读取公开仓库中的 SKILL.md 和配套资料。
7. 在 CHANGELOG.md 记录内容变化，在 evals/results.md 记录验证与未执行项，保留版权边界。先在总目录增加 published 项，再由关联工具更新系列，避免不存在的安装链接。

系列入口、Topics 与推荐不在这里手工维护，均来自总仓库 catalog/skills.json。自动 README 同步由 GitHub Actions 执行；跨仓库 About 管理使用维护者现有 gh 登录，不向 CI 额外配置长期密钥。
