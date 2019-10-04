import os
import logging
import logging.config


def setup_logger():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    log_cfg = os.path.join(root_dir, "setup.cfg")
    logging.config.fileConfig(log_cfg)


setup_logger()
LOGGER = logging.getLogger("geo_deep_learning")
