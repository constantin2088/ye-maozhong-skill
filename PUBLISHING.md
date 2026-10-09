# 发布规范

1. 新事实或引语补 sources.md 的版本、定位、核查日期；方法变化同步 examples 与 evals。
2. 执行 `python scripts/check_skill.py . --release`、`python -m unittest discover -s tests -v` 和 `python scripts/check_links.py`。
3. 按 evals/test-cases.md 记录独立模型回答。未执行必须在结果和 Release 说明中披露，不能声称行为测试通过。
4. 从总目录刷新系列区块：`python scripts/sync_series.py --slug ye-maozhong-skill`。
5. 用已有管理权限同步 About：`python scripts/sync_series.py --slug ye-maozhong-skill --metadata --apply`。先不带 --apply 可预览。
6. 审查差异，提交后确认对应 SHA 的 GitHub CI 全绿；创建带语义版本的 tag 和 Release。文档修订用补丁版本，方法变化用次版本。
7. Release 列出内容、验证、未执行项与版权边界。先在总目录增加 published 项，再由关联工具更新系列，避免不存在的安装链接。

系列入口、Topics 与推荐不在这里手工维护，均来自总仓库 catalog/skills.json。自动 README 同步由 GitHub Actions 执行；跨仓库 About 管理使用维护者现有 gh 登录，不向 CI 额外配置长期密钥。
