from operator import attrgetter

class ReportSet:
    def __init__(self):
        self.report_list = []
    
    def add_report(self, report):
        self.report_list.append(report)

    def print_stats(self):
        for i in self.report_list:
            i.calc_avgs()
        sorted_profit = sorted(self.report_list, key= lambda x: x.average_profit, reverse = True)
        sorted_profit = [i.method for i in sorted_profit]
        sorted_profit_ratio = sorted(self.report_list, key= lambda x: x.average_profit_ratio, reverse = True)
        sorted_profit_ratio = [i.method for i in sorted_profit_ratio]
        sorted_profit_diff = sorted(self.report_list, key= lambda x: x.average_profit_diff)
        sorted_profit_diff = [i.method for i in sorted_profit_diff]
        sorted_lateness = sorted(self.report_list, key= lambda x: x.average_lateness)
        sorted_lateness = [i.method for i in sorted_lateness]
        sorted_lateness_ratio = sorted(self.report_list, key= lambda x: x.average_lateness_ratio)
        sorted_lateness_ratio = [i.method for i in sorted_lateness_ratio]

        print("Dataset: ", self.report_list[0].data_set)
        print("Total Profit Rankings: ", sorted_profit)
        print("Total Profit Ratio Rankings: ", sorted_profit_ratio)
        print("Total Profit Diff Rankings: ", sorted_profit_diff)
        print("Total Lateness Rankings: ", sorted_lateness)
        print("Total Lateness Ratio Rankings: ", sorted_lateness_ratio)


        
