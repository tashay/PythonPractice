import sys

task_list = []

def addTask(description):
    task_list.append(description)
    
def viewTask():
    print ('Tasks:')
    for i in task_list: 
        print (i)
        
def delTask(index):
    del task_list[index]
    
for line in sys.stdin:
    eval(line)
