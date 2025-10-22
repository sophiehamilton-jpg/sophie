# Homework 5: Review


# --- Homework 1 + 2 Review ---

# 3.1 Vocab Review

# 1. Git is an interface for sharing and tracking code. Github hosts Git repositories.
# 2. The terminal is where you access and manipulate files and directories, 
#    the command line is where you actually write the code.
# 3. A local repository is on your device, a remote repository is avaliable online
# 4. Version control is the process of tracking updates and changes within a software.
# 5. The staging area is where your files go before being uploaded remotely.
# 6. Git add adds untracked files to the staging area.
# 7. Git commit saves your files locally.
# 8. Git push saves your files remoteley.
# 9. Git status shows the repository you are currently in.
# 10. Git pull pulls remote files onto your device.
# 11. Pwd displays the directory you are currently in.
# 12. Ls lists the contents of the directory you are currently in.
# 13. Cd changes your directory.
# 14. Nano allows you to view and edit the contents of a file.
# 15. Touch creates a file.
# 16. Mv moves a file.
# 17. Rm removes a file.
# 18. Cat displays file contents.

# 3.2 A Directory Tree

# 1. cd
# 2. ls
# 3. cd ../brianna_repo/
#    git pull
# 4. mv homework.py ~/python_decal/judy_decal/homework/
# 5. cd ../judy_decal/homework/
# 6. ls
# 7. git add
#    git commit -m "finished homework #"
#    git push
# 8. Judy did not commit her files locally before attempting to push.
# 9. cd ~/Recent/


# --- Homework 3 Review ---

# 4.1 Data Types

def checkDataType(input):
    return print(type(input))

checkDataType(3.24)
checkDataType(True)

# 4.2 Conditionals

def evenOrOdd(num):
    if num % 2 > 0:
        print("Odd")
    else:
        print("Even")

evenOrOdd(7)
evenOrOdd(10)

# Loops

def sumWithLoop(my_list):
    total = 0
    for i in my_list:
        total += i
    return print(total)

numbers = [1, 2, 3, 4, 5]
sumWithLoop(numbers)


# --- Homework 4 Review ---

# 6.1 Lists

def duplicateList(my_list):
    new_list = []
    for i in my_list:
        new_list.append(i)
        new_list.append(i)
    return print(new_list)

duplicateList(["a", "b", "c"])

# 6.2 Debugging

# Missing  colon after def square(num)

sumWithLoop([31.6, 40, 6, 12, 79])