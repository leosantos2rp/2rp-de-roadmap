## Trial Annotations
Notes that i can use for consulting.

### Git Commands
- git --version (git version)
- git init (initialize git within the project)
- git add . (add all files to staging - if just one file, filename instead of .)
- git status (yes, git status)
- git commit -m "commit-name" (commit updates)
- git commit -a -m "commit-name" (add and commit in the same command)
- git branch -M "main" (alter master branch name)
- git remote add origin link.git (integrate repository to github)
- git push -u origin main (push repository to github - 'main' means the branch name you're using)
- git branch <branch-name> (create new branch)
- git checkout -b <branch-name> (create new branch and change to it)
- git checkout main (come back to main branch)
- git checkout -m <newbranchname> (rename branch)
- git checkout -m <currentname> <newbranchname> (rename when in another branch)
- git checkout -d <branch-name> (remove branch)
- git push --delete origin <branch-name> (remove branch from server)
- git merge <branch-name> (merge another branch with main branch)
- git clone link.git (clone repository to PC)
- git pull (clone eventual updates from the cloned repository)
- git checkout <filename> (undo file changes and come back to last commit)
- git reset --hard (reset all files to last commit)
- git clean -f (remove untracked files created)
- git clone <foldername>/ <newrepositoryname> (clone)
- git tag -a <tagname> -m "tagmessage" (create tag)
- git tag -a <tagname> <commitsha1> -m "tagmessage" (create tag on specific commit)
- git tag (list)
- git push origin <tagname> (pushing tag to server)
- git checkout <tagname> (using tag)
- git tag -d <tagname> (delete local tag)
- git push --delete origin <tagname> (delete tag from server)
- git stash (save changes in memory)
- git stash list (yes)
- git stash apply (get last stash from the list)
- git stash pop (get last stash and remove from the list)
- git stash pop <stashname> (get specific stash and remove from list)
- git stash drop <stashname> (remove stash from the list)
- git reset --hard HEAD~<number of commits returned> (cancel/return commit)
- git commit --amend (add another change to an existing commit)

### HDFS Commands
- ssh 2rp-leonardos@ocspbasprdap01 (access cluster)
- df (how much space i am utilizing from the hard drive)
- df -h (the same, but formatted)
- hostname (server name)
- hdfs dfs (base command to access the hdfs cluster)
- hdfs dfs -help df (help)
- hdfs dfs -df (similar do df command (-h to formatted info))
- du (size of the directories in use)
- hdfs dfs -ls (list files)
- hdfs dfs -ls -R (files and directories)
- hdfs dfs -ls /user/somedir (list directories/ files under directory)
- sudo -u hdfs (run command as the hdfs user)
- sudo -u hdfs hdfs dfs -mkdir /user (create directory)
- hdfs dfs -mkdir /user/directoryname (create dir under another)
- ls -lrt (local file system)
- hdfs dfs -put <filename> /user/data/<filename> (put file into hdfs)
- tail <filename> (shows last 10 lines of a file)
- hdfs dfs fsck <filepath> (Check a file in cluster)
- hdfs fsck <filepath> -files -blocks (get blocks of the file)
- hdfs fsck <filepath> -files -blocks -locations (get blocks and of the file)
- hdfs dfs -rm <filepath> (remove file)
- hdfs dfs -rm -skipTrash <filepath> (remove permanently)
- hdfs dfs -expunge (clear trash)
- sudo vi <filename.extension> (create file using sudo)
- nano (text editor)
- cat <filename*.extension*> >> <filepath.extension> (append to file)
- cat <filename*.extension*> >> <filepath.extension> overwrites to file)
- hdfs dfs -appendToFile <filename*.ext*> <filepath> (append hdfs files, that is, merge)
- hdfs dfs -tail <filepath> (get file content)
- hdfs dfs -cat <filepath> (get file content)
- hdfs dfs -find . -name "<filename>" (search file by name on current directory)
- hdfs dfs -find . -iname "<filename>" (search file by name on current directory, in-case sensitivy search)
- hdfs dfs -find <filepath> -name "<filename>" (search file by name on specific path)
- hdfs dfs -get <filepathorig> <filepathdest> (copy files from cluster to local server)
- hdfs dfs -getmerge <filepath*> <filepath/filename> (merge match pattern files into one in local fs
- hdfs dfs -count -h -v <filepath> (count files and directories)
- sudo cp <filename> <filepath> (copy files locally)
- mv <filename> <filepath> (move files locally)
- hdfs dfs -cp <filepath> <filepath> (copy files)
- hdfs dfs -mv <filepath> <filepath> (move files)
- hdfs dfs -touchz <filepath> (creates a new file)