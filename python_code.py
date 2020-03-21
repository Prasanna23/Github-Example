Last login: Fri Mar 20 22:25:58 on ttys000
Gayathris-MacBook-Air:~ gayathriviswanathan$ cd ~/Desktop/projects/github-example
Gayathris-MacBook-Air:github-example gayathriviswanathan$ ls
#python_code.py#	README.md
Gayathris-MacBook-Air:github-example gayathriviswanathan$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	#python_code.py#

nothing added to commit but untracked files present (use "git add" to track)
Gayathris-MacBook-Air:github-example gayathriviswanathan$ git add python_code.py
fatal: pathspec 'python_code.py' did not match any files
Gayathris-MacBook-Air:github-example gayathriviswanathan$ git add #python.py
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?
Gayathris-MacBook-Air:github-example gayathriviswanathan$ git add #python.py#
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?
Gayathris-MacBook-Air:github-example gayathriviswanathan$ git add python.py
fatal: pathspec 'python.py' did not match any files
Gayathris-MacBook-Air:github-example gayathriviswanathan$ git add python_code.py 
fatal: pathspec 'python_code.py' did not match any files
Gayathris-MacBook-Air:github-example gayathriviswanathan$ emacs python_code.py

print('first one')





















-uuu:**-F1  python_code.py   All L1     (Python)--------------------------------
Auto-saving...done
