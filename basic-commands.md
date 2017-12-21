# Basic Commands

<a name="git-init" href="#git-init"># </a><b>git init</b>

Create a new git repository

``` bash
# Make current folder a git repo
git init

# Make new-folder a git repo in current folder
git init new-folder

# Make new-folder a git bare repo in current folder
git init --bare new-folder
```

<a name="git-remote" href="#git-remote"># </a><b>git remote</b>

Attaching a remote

``` bash
# Add a remote with the name origin
git remote add origin git@github.com:kdheepak/git-information.git

# Add a remote with the name github
git remote add github git@github.com:kdheepak/git-information.git

# Remove a remote with the name github
git remote rm github

# List all remotes
git remote -v
```

<a name="git-clone" href="#git-clone"># </a><b>git clone</b>

``` bash
# Clone a repository
# Equivalent to the following
# - git init git-training
# - cd git-training
# - git remote add origin git@github.com:kdheepak/git-information.git
# - git branch --set-upstream-to=origin/master master

git clone git@github.com:kdheepak/git-information.git
```

``` bash
# Clone a repository to a new-folder
# Equivalent to the following
# - git init new-folder
# - cd new-folder
# - git remote add origin git@github.com:kdheepak/git-information.git
# - git branch --set-upstream-to=origin/master master

git clone git@github.com:kdheepak/git-information.git new-folder
```

``` bash
# Clone a repository to current folder
# Equivalent to the following
# - git init
# - git remote add origin git@github.com:kdheepak/git-information.git
# - git branch --set-upstream-to=origin/master master

git clone git@github.com:kdheepak/git-information.git .
```

<a name="git-add" href="#git-add"># </a><b>git add</b>

These commands moves changes to the staging area

``` bash
# Adds file
git add file

# Adds folder
git add folder

# Add everything in directory. Try to avoid using this.
git add .

# Adds selected hunks – choose hunks with `y` or `n`, and split hunks with `s`
git add -p
```

<a name="git-diff" href="#git-diff"># </a><b>git diff</b>

``` bash
# Shows diff of all changes line by line in all files between current working directory and previous commit.
git diff

# Shows diff of all changes line by line in single file between current working directory and previous commit.
git diff filename

# Shows diff of all changes line by line in single file between current working directory and previous commit.
git diff filename

# Shows diff of all changes line by line in single file between staged file and current working directory.
git diff --cached filename

# Shows diff of all changes word by word in single file between staged file and current working directory.
git diff filename --word-diff
```

<a name="git-commit" href="#git-commit"># </a><b>git commit</b>

These commands create a commit from the content in the staging area.
Commits must have a subject line. They can optionally have a body message. Think email.

``` bash
# commit changes
git commit # opens editor to enter commit message. Default is vi, type `i` to enter insert mode, and enter the message. Hit `:wq` to save and quit the commit message editor

# commit changes with subject
git commit -m "Subject here"

# commit changes with subject and body
git commit -m "Subject here <Hit Enter>
<Hit Enter>
Body can go here.<Hit Enter>
This can be multiple lines.<Hit Enter>
End the message with a double quote"

# Add more content to previous commit
git add file
git commit -m "Change file"
echo "Fix some changes" >> file
git add file
git commit --amend

# Change a previous commit message. Make sure your staging are is empty
git commit --amend -m "Fixing message of previous commit"
```

Every good commit message should be able to complete the following sentence

> "When applied, this commit will: {{ YOUR COMMIT MESSAGE}}"

For example:

- When applied this commit will : Update README
- When applied this commit will : Revert commit 12345

<a name="git-push" href="#git-push"># </a><b>git push</b>

``` bash
# pushes commits from branch that you are currently on to a remote branch of the same name (based on configuration)
git push

# pushes commits to a remote branch and tracks the branch
# Equivalent to the following
# - git branch --set-upstream-to=origin/branch-name branch-name
# - git push
git push -u origin branch-name

# pushes to override remote. Use with care
git push --force
```

<a name="git-branch" href="#git-branch"># </a><b>git branch</b>

Branch names are just labels.

``` bash
# Switch to branch-name
git checkout branch-name

# Switch to commit hash
git checkout 6ef32f

# Create new branch
git checkout -b new-branch-name
# OR
git branch new-branch

# Create new-branch from commit hash
git branch new-branch 6ea4d3

# Create new-branch from current HEAD location and track remote branch
git branch --track new-branch remote/remote-branch

# delete local
git checkout master
git branch --delete branch-name # cannot be on the same branch-name when you do this

# delete remote
git push origin --delete branch-name

# List all remotes
git branch -a

# Track a remote branch
git branch --set-upstream-to=origin/master master
```

<a name="git-fetch" href="#git-fetch"># </a><b>git fetch</b>

``` bash
# Gets changes from the default remote
git fetch

# Gets changes from github remote
git fetch github
```

**Tip** : use `git lg` after `git fetch` to inspect the history.

<a name="git-merge" href="#git-merge"># </a><b>git merge</b>

``` bash
# Brings changes from branch-name into current branch
git merge branch-name

# Brings changes from branch-name on remote called origin into current branch
git merge origin/branch-name
```

**Tip** : You typically want to use `git fetch origin` before using `origin/branch-name` to ensure you have to latest `origin`.

<a name="git-pull" href="#git-pull"># </a><b>git pull</b>

``` bash
# does a fetch and a merge
# - git fetch
# - git merge origin/master
git pull

# does a fetch and a rebase
# - git fetch
# - git rebase origin/master
git pull --rebase

```

<a name="git-cherry-pick" href="#git-cherry-pick"># </a><b>git cherry-pick</b>

``` bash
# Brings changes from a commit into current branch in a new commit with the name message
git cherry-pick 6ea4d3
```


<a name="common-aliases" href="#common-aliases"># </a><b>Common Aliases</b>

``` bash
# view history
git lg

# view whitespace
git check-whitespace # OR git cw

# delete local and remote
git rm-local-and-remote branch-name # tries to switch to master and deletes local and remote branch-name
```


<a name="useful-commands" href="#useful-commands"># </a><b>Useful Commands</b>

``` bash
# Remove .gitignore files
git ls-files -z --ignored --exclude-standard | xargs -0 git rm -r --cached
git commit -m "Remove .gitignore files"

# Force add an gitignore file
git add --force my/gitignored/file.txt

# Clean current directory of all untracked files, including force clean of directories and gitignored files. Use with care, effectively resets all untracked files in a folder. Use following commands as a safe strategy
git clean -fxd

# Check what will be cleaned before cleaning
git clean -fxd --dry-run

# Interatively clean
git clean -fxdi
```




