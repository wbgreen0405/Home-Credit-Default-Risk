import logging
from src.utils import setup_logging

def test_setup_logging_creates_logger(tmp_path):
    log_file = tmp_path / "test.log"
    setup_logging(str(log_file))
    logger = logging.getLogger("test_logger")
    logger.info("Test log entry")
    with open(log_file, "r") as f:
        contents = f.read()
    assert "Test log entry" in contents
