class GrabIgnoreException(Exception):
    """ GrabIgnore Base Exception. """
    pass


class RequestError(GrabIgnoreException):
    """ Error fetching a resource. """
    pass


class InvalidGitignoreError(GrabIgnoreException):
    """ Invalid gitignore file requested. """
    pass
