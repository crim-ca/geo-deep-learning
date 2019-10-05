import os
import logging
import logging.config
import configparser


def setup_logger():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    log_cfg = os.path.join(root_dir, "setup.cfg")
    cfg = configparser.RawConfigParser()
    cfg.read([log_cfg])
    # replace any escaped '%%()', see: 'setup.cfg'
    for section_name, section in cfg.items():
        for param, value in section.items():
            if "%%" in value:
                cfg.set(section_name, param, value.replace("%%", "%"))
    logging.config.fileConfig(cfg)


setup_logger()
LOGGER = logging.getLogger("geo_deep_learning")
