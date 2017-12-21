# Intermediate Commands

<a name="git-reset" href="#git-reset"># </a><b>git reset</b>

``` bash
# reset is best explained here - https://git-scm.com/blog
git reset HEAD~ --soft # only moves HEAD and branch label
git reset HEAD~ --mixed # (default) moves HEAD, branch label and takes changes from commit to staging area
git reset HEAD~ --hard # moves HEAD, branch label and takes changes from commit to working directory

# The following two are almost identical
git checkout branch-name
git reset --hard branch-name

# Important difference is that checkout does not move branch label, and only moves HEAD. Checkout also will abort if it cannot merge changes on disk.
# The following are NOT identical
git checkout 6ea4d2
git reset --hard 6ea4d2
```

<a name="git-rebase" href="#git-rebase"># </a><b>git rebase</b>

``` bash
# Rebase
git rebase HEAD^5

# Rebase interactively
git rebase -i HEAD^5
```


<a name="git-reflog" href="#git-reflog"># </a><b>git reflog</b>

``` bash
# Show reflog
git reflog
```
