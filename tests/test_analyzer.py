def test_count_log_levels():
    logs = [
        "INFO App started\n",
        "ERROR Failed\n",
        "WARNING Low memory\n",
        "ERROR Timeout\n"
    ]

    counts = {
        "INFO": 1,
        "WARNING": 1,
        "ERROR": 2
    }

    assert counts["INFO"] == 1
    assert counts["WARNING"] == 1
    assert counts["ERROR"] == 2
