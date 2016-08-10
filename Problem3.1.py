import sys

task_list = []

def addTask(description):
    task_list.append(description)
    save_to_file()
    
def viewTask():
    print ('Tasks:')
    for task in task_list:
        print (task)
        
def delTask(index):
    del task_list[index]
    save_to_file()

def save_to_file():
    f = open('to-do_list', 'w')
    for task in task_list:
        f.write(task + '\n')
    f.close()
    
for line in sys.stdin:
    eval(line)

