import json

def log_analyzer():
            try: 
                summary = {
                    "ERROR": 0,
                    "INFO": 0,
                    "WARN": 0   
                }
                # count = 0

                with open("app.log", "r") as file:
                    for line in file:
                        if "ERROR" in line:
                            summary["ERROR"] += 1
                        elif "INFO" in line:
                            summary["INFO"] += 1
                        elif "WARN" in line:
                            summary["WARN"] += 1

                print(summary)

                with open("summary.log", "w") as file:
                    json.dump(summary, file)
            except FileNotFoundError:
                print("The file 'app.log' was not found.")

log_analyzer()