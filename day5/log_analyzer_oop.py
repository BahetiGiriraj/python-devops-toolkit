import pdb
import json

class LogAnalyzer:
        
        def __init__(self, log_file , output_file):
            self.log_file = log_file
            self.output_file = output_file

        def read_logs(self):
            
            with open(self.log_file, "r") as file:
                # print(file.readlines()) 
                return file.readlines() 
            
        def log_analyzer(self ):
            # pdb.set_trace()
            summary = {"INFO": 0, "WARN": 0, "ERROR": 0, "UNKNOWN": 0}
            lines = self.read_logs()
            for line in lines:
                if "INFO" in line:
                    summary["INFO"] += 1
                elif "WARN" in line:
                    summary["WARN"] += 1
                elif "ERROR" in line:
                    summary["ERROR"] += 1
                else:
                    summary["UNKNOWN"] += 1
            return summary


        def write_summary(self,summary):
            with open(self.output_file, "w") as file:
                json.dump(summary, file)



logs = LogAnalyzer("app.log", "summary.json")

logs.log_analyzer()

logs.write_summary(logs.log_analyzer()) 













