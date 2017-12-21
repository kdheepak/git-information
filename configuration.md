# Configuration



``` bash
# Find all .gitconfig locations being used. Windows users - Run in git bash
# Typically found in -
# Windows - C:\Users\JohnDoe\.gitconfig
# MacOS - /home/johndoe/.gitconfig
git config --list --show-origin | awk '{print $1}' | uniq
```


<a name="git-configuration" href="#git-configuration"># </a><b>git configuration</b>

* Open CMD / Git Bash on Windows OR open Terminal or ITerm2 on MacOS
* Type the following and hit enter

``` bash
# Configure user.email
git config --global user.email "$USER@email.com"; # Sets your git user.email to your email, replace $USER with your github.email.com username or to the local-part of your email

# Configure user.name
git config user.name "$FIRSTNAME $LASTNAME";

# Configure default push settings
# - nothing: do not push anything
# - matching: push all matching branches (This is the default in Git 1.x.)
# - upstream: push the current branch to its upstream branch (tracking is a deprecated synonym for upstream)
# - current: push the current branch to a branch of the same name
# - simple: like upstream, but refuses to push if the upstream branch's name is different from the local one (default in 2.0)
git config --global push.default current # recommended

# auto-convert CR for Windows git users
git config --global core.autocrlf true

# Show whitespace
git config --global alias.check-whitespace '!git diff-tree --check $(git hash-object -t tree /dev/null) HEAD'

# Set up better colors
git config --global color.ui true

# Nice log (ADOG)
git log --all --decorate --oneline --graph

# Nicer log
git config --global alias.lg "log --all --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --"

# Commonly used aliases
git config --global alias.df "diff --word-diff"
git config --global alias.dc "diff --cached"

git config --global alias.st "status -s"

git config --global alias.cp "cherry-pick"
git config --global alias.ci "commit"

git config --global alias.co "checkout"
git config --global alias.br "branch"

git config --global alias.r "reset"
git config --global alias.rh "reset --hard"

git config --global alias.sl "stash list"
git config --global alias.sa "stash apply"
git config --global alias.ss "stash save"

# delete local and remote branch
git config --global alias.rm-local-and-remote '!f(){ git checkout master; git branch -D "$1";  git push origin --delete "$1"; };f'


# submodule status
git config --global status.submoduleSummary true
# Remove redundant information for diff in submodule
git config --global diff.submodule log
# add alias for submodule pull. Use with care.
git config --global alias.spull '!git pull && git submodule sync --recursive && git submodule update --init --recursive'
# add alias for submodule push. Use with care.
git config --global alias.spush 'push --recurse-submodules=on-demand'

# rerere
git config --global rerere.enabled true
git config --global rerere.autoupdate true # optional
```

<a name="terminal" href="#terminal"># </a><b>Terminal</b>

**Windows**

- git bash (default)
- [posh-git](http://dahlbyk.github.io/posh-git/)
- ConEmu + git bash

**MacOS**

- Terminal
- ITerm2

<a name="gui" href="#gui"># </a><b>GUI</b>

- [SourceTree](https://www.sourcetreeapp.com/) (free, cross platform)
- [GitExtensions](https://gitextensions.github.io/) (free, open source, Windows only)
- [GitKraken](https://www.gitkraken.com/) (paid, free for trial, cross platform)


