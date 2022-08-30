@echo off

git init
@echo,

ECHO GIT ADD .
git add .
@echo,

ECHO GIT COMMIT
git commit -m "Auto-committed on %date%"
@echo,

ECHO GIT PUSH
git push
@echo,

PAUSE