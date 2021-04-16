from NENV import *


# API METHODS

# self.main_widget()        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------
from numpy import imag


class Imag_Node(Node):
    def __init__(self, params):
        super(Imag_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        imag_matrix = imag(self.input(0))
        self.set_output_val(0, imag_matrix)
        self.main_widget().update_matrix(imag_matrix)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass # ...

    def removing(self):
        pass
