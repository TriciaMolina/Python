class SRTF:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Job ID: "))
            arrival_time = int(input("Enter Arrival Time: "))
            burst_time = int(input("Enter Burst Time: "))
            print()
            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(temporary)
        self.schedulingProcess(process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1]) #sorting based on arrival time
        while True:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                '''
                Sort processes according to Burst Time
                '''
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] -= 1
                if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] -= 1
                if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
        t_time = self.calculateTurnaroundTime(process_data)
        w_time = self.calculateWaitingTime(process_data)
        self.printData(process_data, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]   #turnaround_time = completion_time - arrival_time
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]  #waiting_time = turnaround_time - burst_time
            total_waiting_time = total_waiting_time +waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        process_data.sort(key=lambda x: x[0])   #Sort processes according to the Process ID
        print("Job_ID  Arrival_Time  Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
             for j in range(len(process_data[i])):
                 if j != 2 and j != 3:
                     print(process_data[i][j], end="	    	")
             print()
        print('Average Turnaround Time:', average_turnaround_time)
        print('Average Waiting Time:', average_waiting_time)
        print('Gantt Chart:', sequence_of_process)
