def generate_report(counts):
    report = "\nLog Summary Report\n"
    report += "-" * 20 + "\n"

    for level, count in counts.items():
        report += f"{level}: {count}\n"

    return report
