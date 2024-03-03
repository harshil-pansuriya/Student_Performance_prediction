import sys
import logging

# Defines a function to construct a detailed error message
# Takes the error exception and sys error details as arguments
def error_msg_detail(error, error_detail: sys):

    # Extract traceback info using sys error details
    _, _, exc_tb = error_detail.exc_info()  

    # Get file name from traceback information
    file_name = exc_tb.tb_frame.f_code.co_filename  

    # Construct error message with file name, line number and error message
    error_message = 'Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error))

    # Return the constructed detailed error message 
    return error_message


# Custom Exception class to handle errors in the application
# Extends base Exception class to create a custom exception type
class CustomException(Exception):

    # Initialization method 
    def __init__(self, error_message, error_detail: sys):
        
        # Pass error message to base Exception class
        super().__init__(error_message)  

        # Generate the detailed error message
        self.error_message = error_msg_detail(error_message, error_detail=error_detail)

    # ToString method prints the error message 
    def __str__(self):
        return self.error_message




# Example usage:    
# try:
#     a=1/0
# except Exception as e:   
#     logging.info('Divide by Zero error')
#     raise CustomException(e,sys) #Pass error details to custom exception