import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from log_monitor.analyzer import count_log_levels, filter_logs

def test_count_log_levels():
    logs = [
        "INFO App started\n",
        "ERROR Failed\n",
        "WARNING Low memory\n",
        "ERROR Timeout\n"
    ]

    counts = count_log_levels(logs)

    assert counts["INFO"] == 1
    assert counts["WARNING"] == 1
    assert counts["ERROR"] == 2


def test_filter_logs():
    logs = [
        "INFO App started\n",
        "ERROR Failed\n",
        "ERROR Timeout\n"
    ]

    errors = filter_logs(logs, "ERROR")
    assert len(errors) == 2
