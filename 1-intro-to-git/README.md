# Introduction to Git

Author: Yoseph Kurnia Soenggoro

Date: 8 February 2020

Description: This tutorial provides a brief introduction on using Git without any usage of GitHub. No knowledge on Git is required prior to reading this. However, installation of a version of git will be essential.

### About Git

Git is a free and open source distributed version control system designed to help an individual or a group to manage their programming projects. It helps programmer to track their changes with ease and efficiency.

**One Important thing to note is that Git:**
Git and GitHub are not the same thing and it **SHOULD NOT** be. Git is a version control and works directly with a PC, plus does not require any internet to work. On the other hand, GitHub is a hosting service that works together with Git to provide a platform for sharing open source codes.

### Git Concepts

1. Repository

The place where you store your work. At first, it’s a folder on your computer. When you add version control, the folder becomes a **repository** and can keep track of the changes you make.

2. Branch

Many times you’ll want to explore things or work on your project without having to mess around with the work you have done until that moment.

In that case, a good thing to do is to create a **branch**.

A branch is a deviation from the course of history reflected by `master`. The `master` branch and the new one can evolve differently from that point in history. Some time in the future you could merge them again but, for now, you can change things in one of the branches without affecting the other.

3. Commit

Making changes within the file could be overwhelming when developing an application, libraries, or modules. Therefore, it is essential to track all those changes by use **commit**. Git's commit could be viewed as a history of changes within the repository that can be looked back easily once the commit was made. Within a group setting, it tracks not only the changes within a file that was made, but also when and who make the changes.


### Initial Setup

First, go to the official [Git website](https://git-scm.com/) and install git. After finish the installation setup, check whether it has been successfully installed into your computer by opening the terminal and type the following command.

```
  $ git --version
```

If a version of git was outputted, then the installation is successful. Otherwise, some error occured during installation process.

### Setting Up Local Git Repository

Open your terminal and make a new folder on a designated place. Next step, change your directory to the newly made folder.

```
  $ mkdir <your folder>
  $ cd <your folder>
```

Then, and make a new file `hello-world.py` with the following content.

```
  # hello-world.py
  
  print("Hello World")
```

Within the folder initialize a repository by typing down the following command in the terminal.

```
  $ git init
```

### Managing Git Branches and Making Commits

In order to verify that your git has been successfully initialized, check whether a branch called `master` exists as follows

```
  $ git branch
```

If the list of branches are displayed, which in this case is only `master`, then the initialization is successful. Otherwise, and error message will popup. Now, if you want to have a different version of the same file but do not want to delete the original, then it can be simply done by making a new branch as follows.

```
  $ git checkout -b <new branch name>
```

After the new branch was made, try to check again the list of branches with `git branch`. Then, now you have a copy of all the files from the previous branch, which is `master`. Suppose make some sublte changes to the python file within the folder such as follows.

```
  # hello_wolrd.py
   
  print("Hello Text")
```

Save the file and make a **commit**, which could be used to track your changes. In order to make commit, follow below commands in the terminal.

```
  $ git add .
  $ git commit -m "Initial Commit"
```

After a commit was made, all the changes within the new branch will be recorded and will not affect the `master` branch (or other branches, if you have more). In order to understand what I mean, switch to the `master` branch and you can see into the python file content that is unchanged.

```
  $ git checkout <branch name>
```

### Merging Branches

Within software development, it is common practice to have a branch that stores all the successfully coded files, and the others where changes are made such that the successfully build one does not affect the original. However, in times, programmers want to 'export' the changes to the original branch with successful build to update. Hence, **merging the branches** will be essential. In order to understand more, let's do some merging.

Previously, we had 2 branches, `master` and another branch where changes were made. In order to 'export' those changes into the `master` branch, simply type the following. **MAKE SURE THAT THE CURRENT BRANCH IS `master`**

```
  $ git merge <your branch>
```

Once the process is completed, check the python file within the `master` branch and you can the changes.
