class VersionError(Exception):
    """
    Raised when trying to run application.py with an unsupported python version.
    """
    pass


class StateError(Exception):
    """
    Raised when Waf.work() is called upon a closed or a working instance.
    """
    pass


class EntityShutdown(Exception):
    """
    Raised when an AsyncStream.write() or async for AsyncStream() fails due to the Host being down.
    """
    pass


class EntityShutdownWarning(Warning):
    """
    Raised when an IO operation was called upon a closed connection or entity.
    """
    pass


class AclFetchError(Exception):
    """
    Raised when Access List activity loop fails to fetch from API or backup sources.
    """
    pass


class AclBackUpError(Exception):
    """
    Raised when backup options for a fetching resource isn't available or not found.
    """
    pass