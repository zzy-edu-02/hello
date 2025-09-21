# Git 命令练习指南

这个目录包含了各种Git命令的练习示例和说明。

## 基础Git命令 (Basic Git Commands)

### 1. 仓库初始化和配置
```bash
# 初始化新仓库
git init

# 配置用户信息
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 查看配置
git config --list
```

### 2. 基本工作流程
```bash
# 查看状态
git status

# 添加文件到暂存区
git add <file>
git add .  # 添加所有文件

# 提交更改
git commit -m "提交信息"

# 查看提交历史
git log
git log --oneline  # 简化显示
```

### 3. 分支操作
```bash
# 创建新分支
git branch <branch-name>

# 切换分支
git checkout <branch-name>
# 或者使用新语法
git switch <branch-name>

# 创建并切换到新分支
git checkout -b <branch-name>
# 或者
git switch -c <branch-name>

# 查看所有分支
git branch -a

# 合并分支
git merge <branch-name>

# 删除分支
git branch -d <branch-name>
```

### 4. 远程仓库操作
```bash
# 添加远程仓库
git remote add origin <url>

# 查看远程仓库
git remote -v

# 推送到远程仓库
git push origin <branch-name>

# 从远程仓库拉取
git pull origin <branch-name>

# 克隆仓库
git clone <url>
```

### 5. 撤销和回退
```bash
# 撤销工作区的修改
git checkout -- <file>

# 撤销暂存区的修改
git reset HEAD <file>

# 回退到上一个提交
git reset --soft HEAD~1  # 保留工作区和暂存区
git reset --mixed HEAD~1 # 保留工作区，清空暂存区
git reset --hard HEAD~1  # 清空工作区和暂存区

# 查看操作历史
git reflog
```

## 练习建议

1. 在这个仓库中练习上述命令
2. 创建不同的分支进行实验
3. 尝试合并和解决冲突
4. 练习撤销和回退操作
5. 与远程仓库进行交互

## 进阶练习

- 学习使用 `git rebase`
- 了解 `git cherry-pick`
- 掌握 `git stash` 的使用
- 学习 Git hooks
- 了解 `.gitignore` 的配置