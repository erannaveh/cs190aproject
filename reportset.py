from operator import attrgetter

class ReportSet:
    def __init__(self):
        self.report_list = []
    
    def add_report(self, report):
        self.report_list.append(report)

    def print_stats(self):
        max_total_profit = max(self.report_list, key=attrgetter('total_profit'))
        max_profit_ratio = max(self.report_list, key=attrgetter('profit_ratio'))
        max_profit_diff = max(self.report_list, key=attrgetter('profit_diff'))
        max_lateness = max(self.report_list, key=attrgetter('lateness'))
        max_lateness_ratio = max(self.report_list, key=attrgetter('lateness_ratio'))

        min_total_profit = min(self.report_list, key=attrgetter('total_profit'))
        min_profit_ratio = min(self.report_list, key=attrgetter('profit_ratio'))
        min_profit_diff = min(self.report_list, key=attrgetter('profit_diff'))
        min_lateness = min(self.report_list, key=attrgetter('lateness'))
        min_lateness_ratio = min(self.report_list, key=attrgetter('lateness_ratio'))

        print("Best Total Profit: ", max_total_profit.method)
        print("Worst Total Profit: ", min_total_profit.method)
        print("Best Profit Ratio: ", max_profit_ratio.method)
        print("Worst Profit Ratio: ", min_profit_ratio.method)
        print("Best Profit Difference: ", min_profit_diff.method)
        print("Worst Profit Difference: ", max_profit_diff.method)
        print("Best Lateness: ", min_lateness.method)
        print("Worst Lateness: ", max_lateness.method)
        print("Best Lateness Ratio: ", min_lateness_ratio.method)
        print("Worst Lateness Ratio: ", max_lateness_ratio.method)

        
