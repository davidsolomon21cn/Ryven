from NENV import *

import cv2

# API METHODS

# self.main_widget()        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------


class %CLASS%(Node):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        self.img = self.input(0)
        self.kern = self.input(1)
        self.iter = self.input(2)

        self.res = cv2.dilate(self.img, self.kern, iterations=self.iter)
        self.main_widget().show_image(self.res)

        self.set_output_val(0, self.res)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass # ...


    def remove_event(self):
        pass
