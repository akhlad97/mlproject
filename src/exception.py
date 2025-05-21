import sys  # Provides access to exception details like traceback
import logging  # Used to log messages (info, warning, error, etc.)

# Function to extract detailed error message from exception
def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get the traceback object from exception info
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract filename where exception occurred
    error_message = "error occurred in python script name[{0}] line number[{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Format: filename, line number, error string
    )
    return error_message  # Return the detailed error message

# Custom exception class that inherits from built-in Exception
class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Initialize base Exception class
        self.error_message = error_message_details(error_message, error_detail=error_detail)  # Store detailed message

    def __str__(self):
        return self.error_message  # Return the detailed message when printed

# # Main execution block — runs only when this script is run directly
# if __name__ == "__main__":
#     try:
#         1 / 0  # Intentionally cause a ZeroDivisionError
#     except Exception as e:
#         logging.info('Logging has started')  # Log that logging has started
#         raise CustomException(e, sys)  # Raise custom exception with detailed error info
