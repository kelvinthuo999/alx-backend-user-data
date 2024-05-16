#!/usr/bin/env python3
"""
This module contains the function `filter_datum` for obfuscating specified
fields in log messages.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): A list of strings representing all fields to
                            obfuscate.
        redaction (str): A string representing by what the field will be
                         obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character is
                         separating all fields in the log line.

    Returns:
        str: The obfuscated log message.
    """
    pattern = '|'.join([
        f"{field}=[^{separator}]*" for field in fields
    ])
    return re.sub(
        pattern, lambda x: x.group().split('=')[0] + '=' + redaction, message
    )
