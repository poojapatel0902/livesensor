import sys
import os
def error_message_detail(error,error_detail:sys):#us to detect which line error come
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename#which file error came
    error_message="error occured and the filename is[{0}] and the linenumber is[{1}]and error is[{2}]".format(  #[{0}],[{1}],[{2}] index no
    filename,exc_tb.tb_lineno,str(error))
    return error_message
class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message