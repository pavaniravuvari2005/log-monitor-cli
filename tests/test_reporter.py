from log_monitor.reporter import generate_report


def test_generate_report():
    counts = {
        "INFO": 2,
        "WARNING": 1,
        "ERROR": 3
    }

    report = generate_report(counts)

    assert "INFO: 2" in report
    assert "WARNING: 1" in report
    assert "ERROR: 3" in report
