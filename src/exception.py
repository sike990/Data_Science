import sys
from src.logger import logging

def get_error_detail(error , error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in the python script name[{0}] line number[{1}] file name[{2}]".format(
        str(error),exc_tb.tb_lineno,file_name
    )
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_detail = error_detail
        self.error_message = get_error_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


