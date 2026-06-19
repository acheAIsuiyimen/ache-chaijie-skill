# ache chaijie skill

一个用于小红书账号和竞品拆解的可移植 AI Skill。

它不只总结账号，还会分析内容定位、公开笔记热度、爆款公式、真实封面、可复制点和下一步内容方向。

## 功能

- 用户直接提供 1-5 个账号链接时，立即分析。
- 用户需要找对标时，先用轻量问题明确领域、受众、目标和变现倾向。
- 推荐 2 个成熟标杆和 3 个当前可对标账号。
- 区分主页可见互动数、点赞、收藏和评论，不编造未公开数据。
- 支持单账号深度拆解和 2-5 个账号比较。
- 可输出中文 Markdown 或单页 HTML 可视化报告。

## 使用方式

### 直接分析账号

```text
请分析这个小红书账号：
https://www.xiaohongshu.com/user/profile/EXAMPLE
```

Skill 会直接开始，不强制用户先回答定位问题。

### 先找对标账号

```text
我想做一个职场效率账号，请帮我找适合的小红书对标账号。
```

Skill 会先询问 3-5 个简短问题，再给出 5 个候选账号供用户确认。

## 安装

### Codex 或支持 SKILL.md 的 Agent

1. 下载或 clone 本仓库。
2. 将整个 `ache-chaijie-skill` 目录放入 Agent 的 skills 目录。
3. 确保入口文件名为 `SKILL.md`。

WorkBuddy 或其他 Agent 如果支持从 GitHub 导入 Skill，可直接导入本仓库；如果只支持指令文件，加载 `SKILL.md` 即可。具体安装入口以宿主产品文档为准。

## 可选工具

Skill 不强制依赖某一个插件。如果宿主 Agent 缺少小红书或浏览器读取能力，可考虑：

- [Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- [xiaohongshu-cli](https://pypi.org/project/xiaohongshu-cli/)
- [Playwright](https://playwright.dev/docs/intro)

平台可能需要登录或 Cookie。不要绕过验证码、权限或平台风控。

## 数据与隐私

- 只分析公开可见内容或用户主动提供的数据。
- 无法获取的数据会标注“未公开/未获取”。
- 示例使用虚构用户设定，不包含创建者的公司、履历或私人账号信息。
- 小红书网页结构和反自动化规则可能变化，实际可用数据以运行时为准。

## 仓库结构

```text
ache-chaijie-skill/
├── SKILL.md
└── references/
    └── tools.md
```
