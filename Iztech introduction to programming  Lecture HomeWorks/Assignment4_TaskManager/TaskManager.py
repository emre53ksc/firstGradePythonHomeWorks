# by Emre Kesici - 09.01.2024

def init_tasks():
    return [
        {'id': 1, 'description': "Complete Project Proposal", 'assigned_to': "John Doe", "subtasks": [
            {'id': 2, 'description': "Research", 'assigned_to': "Alice Brown", 'time_estimate': 5},
            {'id': 3, 'description': "Outline", 'assigned_to': "Bob Johnson", 'subtasks': [
                {'id': 4, 'description': "Introduction", 'assigned_to': "Jane Smith", 'time_estimate': 3},
                {'id': 5, 'description': "Body", 'assigned_to': "Jane Smith", 'time_estimate': 6},
                {'id': 6, 'description': "Conclusion", 'assigned_to': "David Wilson", 'time_estimate': 2}
                ]}
        ]}]
        
def add_task_recursive(tasks, selected_taskID, description_input, member_input, time_input):
    new_id = selected_taskID + 1       # The sub-task id needs to be one more than the task it will be sub-tasked with
    
    if selected_taskID == 0:
        new_id = last_id(tasks) + 1         # if new task is not a subtask, then it will be at last line in report
        new_task_dic = {'id': new_id, 'description': description_input, 'assigned_to': member_input, 'time_estimate': time_input}    # new tasks' structure
        tasks = tasks + [new_task_dic]   # tasks is list of dictionary, so new task needs to be last element

    else:           
        for task in tasks:
            if selected_taskID == task['id']:              
                new_task_dic = {'id': new_id, 'description': description_input, 'assigned_to': member_input, 'time_estimate': time_input}
                if 'completed' in task:    # after adding subtask then completed task is no more completed
                    del task['completed']

                if 'subtasks' in task:      #if there are subtasks, it is added to the head of subtasks       
                    task['subtasks'] = [new_task_dic] + task['subtasks']

                else:
                    del task['time_estimate']              # if we add it to a task that has no subtask... 
                    task['subtasks'] = [new_task_dic]      #the time estimate is deleted and the subtask key is created and the new task is put into it

            elif 'subtasks' in task:
                task['subtasks'] = add_task_recursive(task['subtasks'], selected_taskID, description_input, member_input, time_input)
    return tasks

def assign_task(tasks, task_input, new_member):    
    for task in tasks:
        if task['id'] == task_input:        # check id in inital task
            task['assigned_to'] = new_member       # if it is the right task which user want, member will be changed with users input member
        elif 'subtasks' in task:            # if first condition does not hold, check is there a subtasks of initial task
            assign = assign_task(task['subtasks'], task_input, new_member)      # then repeat with subtask 
            if assign:
                return assign
    return None

def modify_id(tasks, description_input, selected_taskID):    # a function for operation 1, to modify ids of after new task
    for task in tasks:    
        if task['description'] != description_input and task['id'] > selected_taskID:  #except new task, increments ids greater than the id entered by the user by 1
            task['id'] = task['id'] + 1
        if 'subtasks' in task:            
            modify = modify_id(task['subtasks'], description_input, selected_taskID)
            if modify:
                return modify
    return None
        
def complete_task_recursive(tasks, id_input):
    for task in tasks:
        if task['id'] == id_input:
            task['completed'] = True       # add a key as completed
            mark_subtasks_as_completed(task.get('subtasks', []))    # if task completed, sub tasks also completed
        elif 'subtasks' in task:
            complete_task_recursive(task['subtasks'], id_input)

def mark_subtasks_as_completed(subtasks):      # a function for mark completed to subtasks, in  complete_task_recursive(tasks, id_input)
    for subtask in subtasks:
        subtask['completed'] = True
        mark_subtasks_as_completed(subtask.get('subtasks', []))

def find_description(tasks, id_input):   # used in operation 2 and 3, for outputting message with description name 
    for task in tasks:
        if task['id'] == id_input:
            return task['description']     # for message to show to user when operation finised
        subtasks = find_description(task.get('subtasks',[]), id_input)
        if subtasks:
            return find_description(task['subtasks'], id_input)
    return None
        
def generate_report_recursive(tasks, level = 0, task_report = ''):
    for task in tasks:
        stripes = level * '--'     # for show the level of tasks
        remain_time, estimated_time = calculate_time_recursive(task, remain_time = 0, estimated_time = 0)
        if remain_time == 0:    # for define satatus
            status = 'completed'
        else:
            status = 'pending'
        task_report += stripes + str(task['id']) + '. ' + task['description'] + '(' + task['assigned_to'] + ') -- Estimated Time to Finish: ' + str(remain_time) + ' out of ' + str(estimated_time) + ' hours, ' + status + '\n'     # structre of each line
        if 'subtasks' in task:
            task_report = generate_report_recursive(task['subtasks'], level + 1, task_report)       # stripes will be increase while going deep
    return task_report

def calculate_time_recursive(task, remain_time = 0, estimated_time = 0):   # calculates each tasks remain time and estimated time
    if 'subtasks' in task:
        for subtask in task['subtasks']:
            remain_time, estimated_time = calculate_time_recursive(subtask, remain_time, estimated_time)
    else:
        estimated_time += task['time_estimate']
        if 'completed' not in task:         # if task is completed, then estimated time do not added to remain time
            remain_time += task['time_estimate']
    return remain_time, estimated_time

def show_tasks_str(tasks, level = 0, show_tasks = ''):               # a funciton for showing initial tasks with their team member, used in operation 1, 2 ,and 3
    for task in tasks:
        stripes = level * '--'
        show_tasks += stripes + str(task['id']) + '. ' + task['description'] + '(' + task['assigned_to'] + ')\n'        # structre of each line
        if 'subtasks' in task:
            show_tasks = show_tasks_str(task['subtasks'], level + 1, show_tasks)       # stripes will be increase while going deep
    return show_tasks

def last_id(tasks):                              # a small function for find last id (and also biggest id)...
    for task in tasks:                           # if user select '0. New Task' when add task operation...
        lastID = task['id']                      # new tasks' id must 1 more then inital last id
        if 'subtasks' in task:
            lastID = last_id(task['subtasks'])
    return lastID

def total_times_msg(tasks, tot_rem_time = 0, tot_estimated_time = 0):   # uses calculate_time_recursive() for total project time
    for task in tasks:                                                  # used in operation 4
        remain_time, estimated_time = calculate_time_recursive(task, remain_time = 0, estimated_time = 0)
        tot_rem_time += remain_time
        tot_estimated_time += estimated_time
    message =  '\nThe total time of the project is: ' + str(tot_estimated_time) + '\n' + 'The remaining time of the tasks to finish the project is: ' + str(tot_rem_time)
    return message

def main():
    tasks = init_tasks()
    operation = 0
    while operation != 5 :
        print('Operations:\n','1. Add a new task\n','2. Assign a task to a team member\n','3. Complete a task\n','4. Generate report\n','5. Exit\n', sep='    ')
        operation = 0
        while operation not in [1,2,3,4,5]:    
            operation = int(input('Please select an operation: '))

        if operation == 1:
            print('0. New Task')
            print(show_tasks_str(tasks, level = 0, show_tasks = ''))
            print()
            selected_taskID = int(input('To add a new task, enter 0. To add a subtask, select the task ID: '))
            description_input = input('Please enter the task description: ')
            member_input = input('Please enter the task responsible: ')
            time_input = int(input('Please enter the estimated time for the task:'))
            tasks = add_task_recursive(tasks, selected_taskID, description_input, member_input, time_input)
            if selected_taskID != 0:     # if input is zero then do not increase ids
                modify_id(tasks, description_input, selected_taskID)
            print(description_input + ' is added.')

        if operation == 2:
            print(show_tasks_str(tasks, level = 0, show_tasks = ''))
            print()
            task_input = int(input('Please select a task: '))
            new_member = input('Please enter the new team members name: ')            
            assign_task(tasks, task_input, new_member)
            message = 'Task ' + find_description(tasks, task_input) + ' assigned to ' + new_member
            print(message)

        if operation == 3:
            print(show_tasks_str(tasks, level = 0, show_tasks = ''))
            print()
            id_input = int(input('Enter task ID:'))
            complete_task_recursive(tasks, id_input)
            msg_description = find_description(tasks, id_input)
            print('Task '+ '\'' + msg_description + '\'' +' marked as completed.')

        if operation == 4:
            report = generate_report_recursive(tasks)
            print(report)
            print(total_times_msg(tasks, tot_rem_time = 0, tot_estimated_time = 0))

        if operation != 5:
            enter = input('Please press enter to continue.\n')
    
if __name__ == "__main__":
    main()
