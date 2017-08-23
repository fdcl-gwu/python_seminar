#!/usr/bin/env python
from traits.api import *
from traitsui.api import *
import logging

class PrintLog(HasTraits):
    levels = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

    levelui = Enum(levels.keys())

    traits_view = View(
        Item('levelui', show_label=False,),
        width=100,
        height=50,
        resizable=True
    )

    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    def _levelui_changed(self):
        print('='*10 + self.levelui)
        level = self.levels.get(self.levelui, logging.NOTSET)
        self.logger.setLevel(level)
        self.print_log()
    def print_log(self):
        self.logger.debug('This is a debug message')
        self.logger.info('This is an info message')
        self.logger.warning('This is a warning message')
        self.logger.error('This is an error message')
        self.logger.critical('This is a critical error message')

if __name__ == '__main__':
    log_obj = PrintLog()
    log_obj.configure_traits()
