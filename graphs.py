import matplotlib.pyplot as plt
from datetime import datetime
class graphing_data:
    def __init__(
        self,
        dataset_path="/Users/andreamurillo/Desktop/VIP/QCM/dataset1.txt"
    ):
        self.dataset_path = dataset_path
    def read_dataset(self):
        data_temp1 = []
        data_temp2 = []
        with open(self.dataset_path, "r") as file:
            for line in file:
                pretemp1 = []
                pretemp2 = []
                if "None" in line:
                    break
                else:
                    pre = line.rstrip().split(",")
                    time = pre[0]
                    pretemp1.append(time)
                    pretemp1.append(pre[1])
                    pretemp2.append(time)
                    pretemp2.append(pre[2])
                data_temp1.append(pretemp1)
                data_temp2.append(pretemp2)
        return data_temp1, data_temp2

    def graph(self):
        data_temp1, data_temp2 = self.read_dataset()
        length = len(data_temp1)
        time_str = ''
        temp1 = []
        temp2 = []
        for ind in range(length):
            time_str = data_temp1[ind][0]
            pt = datetime.strptime(time_str,'%H:%M:%S')
            print(pt)
            times = pt.second + pt.minute*60 + pt.hour*3600
            temp1.append(data_temp1[ind][1])
        for i in range(length):
            temp2.append(data_temp2[ind][1])

        # plotting temp1
        plt.plot(times, temp1)
        plt.xlabel('Time (s)')
        plt.ylabel('Temperature 1 (C°)')
        plt.title('Temp1 vs Time')
        plt.show()
        '''
        # plotting temp2
        temp2_graph = plt.plot(time, temp2)
        temp2_graph.xlabel('Time (s)')
        temp2_graph.ylabel('Temperature 2 (C°)')
        temp2_graph.title('Temp2 vs Time')
        temp2_graph.show()
        '''
if __name__ == "__main__":
    graphing = graphing_data()
    graphing.graph()