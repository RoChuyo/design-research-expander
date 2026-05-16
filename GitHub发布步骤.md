# GitHub 发布步骤

本项目已经安装并配置了 GitHub CLI (`gh`)。你只需要完成一次 GitHub 登录，然后运行发布脚本。

## 1. 登录 GitHub

在终端中进入项目目录：

```bash
cd /Users/lin/Documents/Playground/design-research-expander
gh auth login
```

推荐选择：

```text
GitHub.com
HTTPS
Login with a web browser
```

然后根据终端提示打开浏览器，输入一次性验证码并授权。

## 2. 发布到 GitHub

登录完成后运行：

```bash
./发布到GitHub.sh
```

默认会创建公开仓库：

```text
design-research-expander
```

如果想换名字：

```bash
./发布到GitHub.sh my-repo-name public
```

如果想先创建私有仓库：

```bash
./发布到GitHub.sh design-research-expander private
```

## 3. 发布后建议设置

仓库创建后，打开 GitHub 页面，在右侧 About 区域使用：

```text
Codex Skill for expanding product design research proposals with Chinese literature/case synthesis, direction exploration, workload estimation, and organized research archives.
```

推荐 Topics：

```text
codex-skill, product-design, design-research, industrial-design, cmf-design, research-assistant, chinese, literature-review, case-study, human-centered-design, universal-design
```

## 4. 如果发布失败

检查登录状态：

```bash
gh auth status
```

检查远程仓库：

```bash
git remote -v
```

重新推送：

```bash
git push -u origin main
```
