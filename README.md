<div align="center">

# 🤖 AstrBot-Skill

**AstrBot SKILL · 让 AI 成为你的插件开发助手**

_✨ 结构化技术文档 + AGENT SKILL 定义，赋能 AI 辅助开发 ✨_

[![GitHub Stars](https://img.shields.io/github/stars/EterUltimate/AstrBot-Skill?style=for-the-badge&logo=github&color=yellow)](https://github.com/EterUltimate/AstrBot-Skill)
[![GitHub Forks](https://img.shields.io/github/forks/EterUltimate/AstrBot-Skill?style=for-the-badge&logo=github&color=blue)](https://github.com/EterUltimate/AstrBot-Skill/fork)
[![QQ群](https://img.shields.io/badge/QQ群-1054962131-pink?style=for-the-badge&logo=tencent-qq&logoColor=white)](https://qm.qq.com/q/AstrBot)

</div>

---

## 🎯 这是什么？

AstrBot 的 **AGENT SKILL 仓库**，包含插件开发的结构化技术文档和 Skill 定义。

通过加载本仓库的 Skill，AI 可以：

- 🧠 理解 AstrBot 插件架构和 API
- 📝 生成符合规范的插件代码
- 🔧 提供准确的开发建议和调试帮助
- 📖 编写 AI 友好的技术文档

---

## 🚀 快速开始

### CLI 自动安装（推荐）

使用官方开放 Skills CLI 安装到已支持的本地 Agent：

```bash
npx skills add EterUltimate/AstrBot-Skill -g -y
```

安装到指定 CLI：

```bash
npx skills add EterUltimate/AstrBot-Skill -g -a codex -y
npx skills add EterUltimate/AstrBot-Skill -g -a claude-code -y
npx skills add EterUltimate/AstrBot-Skill -g -a gemini-cli -y
```

也可以先查看仓库里可安装的 Skill：

```bash
npx skills add EterUltimate/AstrBot-Skill --list
```

`npx skills add` 支持 Codex、Claude Code、Gemini CLI、Cursor、OpenCode、Qwen Code 等多个 Agent，并会安装到对应官方 skills 目录。
本仓库的可安装 Skill 位于 `docs/`，CLI 会自动发现 `docs/SKILL.md` 并只安装这份文档目录，避免把仓库脚本、CI 配置或构建产物复制进客户端 skills 目录。

指定版本安装：

```bash
npx skills add EterUltimate/AstrBot-Skill#v1.0.0 -g -y
```

> `npx skills add` 推荐使用仓库源或 `#tag` 源；release zip 产物用于 AstrBot 面板上传，不建议作为 CLI 安装源。

### 让 AI 一键安装

把下面这段发给当前 AI 助手即可：

```text
请帮我安装 AstrBot 开发 Skill。

要求：
1. 先检查 `node --version`、`npm --version`、`npx --version`。
2. 如果没有 Node.js/npm/npx，请先停止并告诉我：需要安装 Node.js 18+ 后才能使用 `npx skills add`；不要假装已经安装成功。
3. 运行 `npx -y skills@1.5.5 add EterUltimate/AstrBot-Skill --list`，确认能发现 `skill-astrbot-dev`。
4. 如果当前是 Codex，运行 `npx -y skills@1.5.5 add EterUltimate/AstrBot-Skill -g -a codex -y`。
5. 如果当前是 Claude Code，运行 `npx -y skills@1.5.5 add EterUltimate/AstrBot-Skill -g -a claude-code -y`。
6. 如果当前是 Gemini CLI，运行 `npx -y skills@1.5.5 add EterUltimate/AstrBot-Skill -g -a gemini-cli -y`。
7. 如果不确定当前客户端，运行 `npx -y skills@1.5.5 add EterUltimate/AstrBot-Skill -g -y`，按 skills-cli 自动检测或提示选择。
8. 安装后告诉我目标目录和 `skill-astrbot-dev` 是否已安装成功。

不要使用 release zip 作为 `npx skills add` 的 source；zip 只用于 AstrBot 面板上传。
如果当前环境不能安装 Node.js，请改走手工兜底：下载仓库，将 `docs/` 目录作为完整 Skill 根目录复制到目标客户端的 skills 目录，并命名为 `skill-astrbot-dev`。
```

### AstrBot 面板安装

从 Releases 下载 `skill-astrbot-dev-<version>.zip`，在 AstrBot 管理面板
`插件 -> Skills` 直接上传即可。

如果是刚推送的新版本 tag，也可以在 GitHub Actions 的 `Tag Build` 运行结果里下载
`skill-astrbot-dev-<tag>` artifact，里面包含可直接上传的 zip。

### 本仓库本地安装

在仓库根目录运行：

```bash
npx skills add . -g -y
```

安装到指定 CLI：

```bash
npx skills add . -g -a codex -y
```

### 本地打包

```bash
python scripts/package_skill.py
```

生成的 `dist/skill-astrbot-dev.zip` 可以直接上传到 AstrBot 或解压到本地 skills 目录。

### 自动构建产物

Tag push（`v*`）会触发 `Tag Build`，自动构建并上传：

- `skill-astrbot-dev-<tag>`: AstrBot Skills 可上传 zip。
- `astrbot-skill-docs-<tag>`: VitePress 静态文档构建产物。

### 使用示例

> 请使用 `skill-astrbot-dev`，然后帮我写一个 AstrBot 插件，实现：当收到消息时自动回复"你好！"

---

## 📚 文档结构

```
docs/
├── SKILL.md              # ⭐ skill-astrbot-dev 定义文件
├── index.md              # 文档索引入口
├── design_standards/     # 核心概念、架构、最佳实践
├── agent/                # Agent 系统（工具/子智能体/沙盒/定时任务）
├── messages/             # 消息模型、事件、组件
├── plugin_config/        # 插件配置、装饰器、生命周期、Hooks
├── platform_adapters/    # 平台适配器接口
├── Storage & Utils/      # 存储与工具类
└── snapshots/            # 版本快照（v4.11.2, v4.12.x...）

data/skills/
└── docs4agent/
    └── index.md          # 文档写作规范参考
```

---

## 🔗 相关链接

| 资源 | 链接 |
|:----:|:----:|
| 📖 官方文档（实时） | [AstrBot 主仓库 docs/](https://github.com/AstrBotDevs/AstrBot/tree/master/docs) |
| 🏠 AstrBot 主仓库 | [github.com/AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) |
| 📝 官方文档站 | [docs.astrbot.app](https://docs.astrbot.app/) |
| 🐛 问题反馈 | [GitHub Issues](https://github.com/AstrBotDevs/AstrBot/issues) |

---

## 🤝 加入社区

[官方交流群 **1054962131**](https://qm.qq.com/q/AstrBot)

### 本地测试

```bash
python scripts/test_api.py
```

---

## 📜 许可证

本项目为 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的文档同步归档，仅供学习参考。

<div align="center">

**⭐ 如果这个项目对你有帮助，请给一个 Star 支持一下！⭐**

Made with ❤️ by AstrBot Community

</div>
