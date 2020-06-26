"""
Library for launching tasks in parallel environment. Task is launched from
command line using ``runjob`` command:

.. code-block:: bash

    runjob [-s SETTINGS] [--disable-one-instance] [--run-once]
           [--sleep-interval SLEEP_INTERVAL] [--run-interval RUN_INTERVAL]
           [--keep-lock]
           task_cls

    runjob -s myapp.settings myapp.task.HelloWorld --run-once

    export JOBSLIB_SETTINGS_MODULE="myapp.settings"
    runjob myapp.task.HelloWorld --run-once

Task is normally run in infinite loop, delay in seconds between individual
launches is controlled by either ``--sleep-interval`` or ``--run-interval``
argument. ``--sleep-interval`` is interval in seconds, which is used to
sleep after task is done. ``--run-interval`` tells that task is run every
run interval seconds. Both arguments may not be used together. `--keep-lock`
argument causes that lock will be kept during sleeping, it is useful when you
have several machines and you want to keep the task still on the same machine.
If you don't want to launch task forever, use ``--run-once`` argument. Library
provides locking mechanism for launching tasks on several machines and only
one instance at one time may be launched. If you don't want this locking, use
``--disable-one-instance`` argument. All these options can be set in
**settings** module. Optional argument ``--settings`` defines Python's
module where configuration is stored. Or you can pass settings module
using ``JOBSLIB_SETTINGS_MODULE``.

During task initialization instances of the :class:`Config` and
:class:`Context` classes are created. You can define your own classes in the
**settings** module. :class:`Config` is container which holds configuration.
:class:`Context` is container which holds resources which are necessary for
your task, for example database connection. Finally, when both classes are
successfuly initialized, instance of the task (subclass of the
:class:`BaseTask` passed as ``task_cls`` argument) is created and launched.

If you want to write your own task, inherit :class:`BaseTask` class and
override :meth:`BaseTask.task` method. According to your requirements
inherit and override :class:`Config` and/or :class:`Context` and set
**settings** module.
"""

from .cmdlineparser import argument
from .config import Config, ConfigGroup, option
from .context import Context, cached_property
from .metrics import BaseMetrics
from .oneinstance import OneInstanceWatchdogError
from .tasks import BaseTask
from .version import VERSION

__all__ = [
    'argument', 'Config', 'ConfigGroup', 'option', 'Context',
    'cached_property', 'BaseMetrics', 'OneInstanceWatchdogError',
    'BaseTask'
]

__version__ = VERSION
