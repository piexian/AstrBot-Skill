<div align="center">

# 🤖 AstrBot-Skill

**AstrBot SKILL · 让 AI 成为你的插件开发助手**

_✨ 结构化技术文档 + AGENT SKILL 定义，赋能 AI 辅助开发 ✨_

[![GitHub Stars](https://img.shields.io/github/stars/EterUltimate/AstrBot-Skill?style=for-the-badge&logo=github&color=yellow)](https://github.com/xunxiing/AstrBot-Skill)
[![GitHub Forks](https://img.shields.io/github/forks/EterUltimate/AstrBot-Skill?style=for-the-badge&logo=github&color=blue)](https://github.com/xunxiing/AstrBot-Skill/fork)
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

### 方式一：使用 npm 安装（推荐）

通过 [skills.sh CLI](https://skills.sh) 安装：

```bash
# 安装到当前项目
npx skills add xunxiing/AstrBot-Skill

# 或全局安装（所有项目可用）
npx skills add -g xunxiing/AstrBot-Skill
```

### 方式二：下载文件

从 [Release](https://github.com/xunxiing/AstrBot-Skill/releases) 下载 Skill 文件，将 `skill-astrbot-dev/SKILL.md` 内容提供给 AI 助手即可激活。

### 示例

> 请阅读 `skill-astrbot-dev/SKILL.md`，然后帮我写一个 AstrBot 插件，实现：当收到消息时自动回复"你好！"

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

data/skills/
└── docs4agent/
    └── SKILL.md          # ⭐ docs4agent 定义文件
```

---

## 🔗 相关链接

| 资源 | 链接 |
|:----:|:----:|
| 🏠 AstrBot 主仓库 | [github.com/AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) |
| 📝 官方文档站 | [docs.astrbot.app](https://docs.astrbot.app/) |
| 🐛 问题反馈 | [GitHub Issues](https://github.com/AstrBotDevs/AstrBot/issues) |

---

## 🤝 加入社区

[官方交流群 **1054962131**](https://qm.qq.com/q/AstrBot)



---

## 📜 许可证

本项目为 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的文档同步归档，仅供学习参考。

<div align="center">

**⭐ 如果这个项目对你有帮助，请给一个 Star 支持一下！⭐**

Made with ❤️ by AstrBot Community

</div>
