from log_monitor.parser import read_logs


def test_read_logs(tmp_path):
    log_file = tmp_path / "sample.log"
    log_file.write_text(
        "INFO App started\n"
        "ERROR Something failed\n"
    )

    logs = read_logs(str(log_file))

    assert len(logs) == 2
    assert logs[0].startswith("INFO")
    assert logs[1].startswith("ERROR")
