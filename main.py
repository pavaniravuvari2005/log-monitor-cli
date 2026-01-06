import argparse
from log_monitor.parser import read_logs
from log_monitor.analyzer import count_log_levels, filter_logs
from log_monitor.reporter import generate_report

VALID_LEVELS = {"INFO", "WARNING", "ERROR"}

def main():
    parser = argparse.ArgumentParser(description="Log Monitor CLI Tool")
    parser.add_argument("file", help="Path to log file")
    parser.add_argument("--filter", help="Filter logs by level (INFO, WARNING, ERROR)")

    args = parser.parse_args()

    logs = read_logs(args.file)
    if not logs:
        return

    if args.filter:
        level = args.filter.upper()
        if level not in VALID_LEVELS:
            print("Error: Invalid log level. Use INFO, WARNING, or ERROR.")
            return

        filtered = filter_logs(logs, level)
        for log in filtered:
            print(log.strip())
    else:
        counts = count_log_levels(logs)
        print(generate_report(counts))

if __name__ == "__main__":
    main()
