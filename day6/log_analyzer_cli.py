import argparse
import json

class LogAnalyzer:
    def __init__(self, log_file, output_file):
        self.log_file = log_file
        self.output_file = output_file

    def read_logs(self):
        with open(self.log_file, "r") as file:
            return file.readlines() 
        
    def log_analyzer(self):
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

    def write_summary(self, summary):
        with open(self.output_file, "w") as file:
            json.dump(summary, file, indent=4)  # Added indent for clean JSON formatting

# logs = LogAnalyzer("app.log", "summary.json")

# logs.log_analyzer()

# logs.write_summary(logs.log_analyzer()) 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log_file", type=str, required=True, help="Path to the log file")
    parser.add_argument("--output_file", type=str, required=True, help="Path to the output summary file")
    args = parser.parse_args()

    analyzer = LogAnalyzer(args.log_file, args.output_file)
    summary = analyzer.log_analyzer()
    analyzer.write_summary(summary)


if __name__ == "__main__":
    main()

