from typing import Optional


class EarlyAttributeAccess(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(message or "An access was accessed before intended.")


class NoFunctionReuse(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(message or "The function you called cannot be called again.")


class FunctionNotAvailableInState(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(
            message
            or "The function you called cannot be called in the current state of the object."
        )
