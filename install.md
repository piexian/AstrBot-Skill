# 安装 `skill-astrbot-dev`

## 方式一：CLI 自动安装（推荐）

使用官方开放 Skills CLI 安装到已支持的本地 Agent：

```bash
npx skills add EterUltimate/AstrBot-Skill -g -y
```

`npx` 依赖 Node.js/npm。安装前请先确认：

```bash
node --version
npm --version
npx --version
```

如果环境没有 Node.js/npm/npx，需要先安装 Node.js 18+；不能使用 npm 的环境请改用 AstrBot 面板 zip 或手工安装兜底。

安装到指定 CLI：

```bash
npx skills add EterUltimate/AstrBot-Skill -g -a codex -y
npx skills add EterUltimate/AstrBot-Skill -g -a claude-code -y
npx skills add EterUltimate/AstrBot-Skill -g -a gemini-cli -y
```

常用参数：

- `-g, --global`: 安装到用户全局 skills 目录。
- `-a, --agent`: 指定目标 CLI，例如 `codex`、`claude-code`、`gemini-cli`。
- `--list`: 只列出仓库内可安装的 Skill，不安装。
- `-y, --yes`: 跳过确认提示。

本仓库的可安装 Skill 位于 `docs/`，CLI 会自动发现 `docs/SKILL.md` 并只安装这份文档目录，避免把仓库脚本、CI 配置或构建产物复制进客户端 skills 目录。

Tag push（`v*`）会触发 `Tag Build`，自动构建可下载产物。

## 方式二：AstrBot 管理面板上传

AstrBot 面板上传仍推荐使用 release 附件里的 `skill-astrbot-dev-<version>.zip`。这个压缩包已经把
`docs/` 内容整理成标准 Skill 目录，解压后的顶层目录就是 `skill-astrbot-dev/`，
不需要再手动复制、重命名或重新压缩。

1. 打开本仓库 Releases。
2. 下载 `skill-astrbot-dev-<version>.zip`。
3. 进入 AstrBot 管理面板 `插件 -> Skills`。
4. 直接上传这个 zip。

如果 release 附件还没发布，可以打开 GitHub Actions 里的 `Tag Build`，下载
`skill-astrbot-dev-<tag>` artifact，其中包含同样可上传的 zip。

上传包结构应为：

```text
skill-astrbot-dev/
├── SKILL.md
├── index.md
├── agent/
├── design_standards/
├── messages/
├── platform_adapters/
├── plugin_config/
└── ...
```

## 方式三：从本地仓库安装到 CLI

在仓库根目录运行：

```bash
npx skills add . -g -y
```

指定 Codex：

```bash
npx skills add . -g -a codex -y
```

## 方式四：本地打包后安装 AstrBot

需要自己生成上传包时，在仓库根目录运行：

```bash
python scripts/package_skill.py
```

生成文件：

```text
dist/skill-astrbot-dev.zip
```

这个 zip 可以直接上传到 AstrBot。

## 手工安装兜底

如果不能使用 `npx skills add` 或 AstrBot release 包，手工复制时只需要遵守一个规则：把仓库的 `docs/` 目录作为完整
Skill 根目录使用，并命名为 `skill-astrbot-dev`。不要只复制 `SKILL.md`。

## 使用提示

安装后可以这样提示 AI：

```text
请使用 skill-astrbot-dev。先读取 SKILL.md，再按其中引用继续读取相关文档。
```

## 验证

- Skill 列表中能看到 `skill-astrbot-dev`。
- AI 能读取 `SKILL.md`。
- AI 能继续访问 `index.md`、`agent/`、`plugin_config/` 等同级文档目录。
