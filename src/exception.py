import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"Error Occoured in Python Script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message

import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()
        self.filename = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno

    def __str__(self):
        return f"Error occurred in script: [{self.filename}] at line [{self.lineno}] - {self.error_message}"
