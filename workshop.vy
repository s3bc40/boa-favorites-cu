# pragma version 0.4.0
# @licence MIT
"""
@author s3bc40
@notice 
    Workshop from Titanoboa course CU. The goal is to
    deploy locally a contract that can set a bool
    and retrieve it on Anvil & Tenderly
"""

# State variables
_my_bool: bool

# Constructor
@deploy
def __init__():
    self._my_bool = False

@external
def set_bool(status: bool):
    """
    @dev Setting new status for boolean
    """
    self._my_bool = status


@view
@external
def get_bool() -> bool:
    """
    @dev Getting the boolean current value
    """
    return self._my_bool
