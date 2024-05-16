#!/usr/bin/env python3
"""
This module contains the function `filter_datum` for obfuscating specified
fields in log messages.
"""

import re
import logging
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


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with the given fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record to filter values of specified fields.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
