# How to contribute code to each week's project.

### Step 1 (only done once!):

Clone the SPICED repository onto your local machine, then go into the folder locally.

- ``git clone <url-of-the-git-repo>``
- ``cd <git-repo>``

### Step 2 (also only done once!)

Create your own branch inside the repository (while simultanously copying the contents of master into your branch).

- ``git checkout -b <your-name> origin/master``

### Step 3 (recurrent process)

Throughout each week (daily, ideally!), you will:

1. **Make changes inside your branch.**
  - always make sure you are on your own branch!

    - ``git branch`` to see all branches, including which one you're currently on.

    - ``git checkout <name-of-branch>`` to switch to another branch.

2. After you've made some sort of change (e.g. added a file, edited a file), **add those changes to the staging area**.

  - ``git add <name-of-file>``

  - (alternatively, ``git add . `` to add everything.)

3. After you've added your changes to the staging area, **commit your changes locally**.

  - ``git commit -m "write your commit message here"``


4. After your changes have been committed locally, **push your changes remotely (on your remote branch)!**.

  - ``git push origin master``

---

### Tips / More Info:

- Run ``git remote -v`` to make sure your local repository has a remote counterpart.

  - By convention, the "name" of the remote version of the repository is called "origin". This doesn't have to be the case, but to avoid confusion, stick to this convention!


- Run ``git pull origin <name-of-branch> `` to synchronize your local branch with the latest changes.

  - This probably won't really apply for you, since you will be the only person working on your branch (therefore always have the latest version). But when we do team projects, this will become critical!


- Always **pull** before you **push**!

  - again, won't really apply to you for the most part during this course, but this is a really good rule-of-thumb when collaborating with others.


- There is another way to make an already existing folder into a git repository (i.e. ``git init``, followed by ``git remote add origin <url-of-git-repo>``), but let's hold off on that for now!!

- Although we are using branches in this course, we are not really using them for their intended purpose (i.e. eventually merging branches). However, we will cover merging later in the course in the software engineering chapter (or, if there's interest in doing  team project). At the moment, the branches are just used for us to keep track of everybody's progress and for you to practice using git!
