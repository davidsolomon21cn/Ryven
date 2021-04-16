from NWENV import *
from PySide2.QtWidgets import QTextEdit
from PySide2.QtGui import QFontMetrics

import numpy as np


class MatrixWidget(QTextEdit, MWB):

    def __init__(self, params, base_width=50, base_height=50):
        MWB.__init__(self, params)
        QTextEdit.__init__(self)

        c = self.node.color
        self.setStyleSheet('''
QTextEdit{
    color: '''+c+''';
    background: transparent;
    border: none;
    border-radius: 4px;
    padding: 0px;
    font-family: Source Code Pro;
    font-size: 10pt;
}
        ''')  
        # border: 1px solid '''+c+''';
        
        # self.setFont(font)
        self.base_width = base_width
        self.base_height = base_height
        self.setFixedSize(self.base_width, self.base_height)
        self.setReadOnly(True)
        self.hidden_size = None

    def update_matrix(self, m):
        if m is None:
            self.setText('')
            return

        longest_exp_length = -1
        lines = []

        try:
            matrix = np.around(m, 4)
        except Exception:
            matrix = m

        if matrix.ndim == 0:    # scalars
            lines = [str(m)]

        elif matrix.ndim == 1:
            longest_exp_length = self.get_row_lxl(matrix)
            row = matrix
            lines.append(self.format_row_to_str(row, longest_exp_length))

        elif matrix.ndim == 2:
            for row in matrix:
                nlxl = self.get_row_lxl(row)
                if nlxl > longest_exp_length:
                    longest_exp_length = nlxl

            for row in matrix:
                lines.append(self.format_row_to_str(row, longest_exp_length))


        s = '\n'.join(lines)
        self.setText(s)
        self.resize_to_content(lines)

    def get_row_lxl(self, row):
        longest_exp_length = -1
        for exp in row:
            if type(exp) == str:
                if len(exp) > longest_exp_length:
                    longest_exp_length = len(exp)
            else:
                if len(str(exp)) > longest_exp_length:  # round(number, 4)
                    longest_exp_length = len(str(exp))
        return longest_exp_length

    def format_row_to_str(self, row, lxl):
        format_str = len(row) * ('{:>'+str(lxl)+'} ')
        format_str = format_str[:-1]
        return format_str.format(*row)

    def resize_to_content(self, lines):
        if len(lines) == 0:
            lines.append('')

        # resize properly
        fm = QFontMetrics(self.font())
        text_width = fm.width(lines[0]+('_'*2))
        text_width = text_width+20  # some buffer
        text_height = fm.height()*(len(lines))+15  # vertical buffer for padding etc.
        self.setFixedWidth(text_width if text_width > self.base_width else self.base_width)
        self.setFixedHeight(text_height if text_height > self.base_height else self.base_height)
        self.node.update_shape()

    def hide(self):
        self.hidden_size = self.size()
        self.setFixedSize(0, 0)
        self.node.update_shape()

    def show(self):
        self.setFixedSize(self.hidden_size)
        self.node.update_shape()
        self.hidden_size = None


    def get_state(self):
        data = {'text': self.toPlainText(),
                'shown': self.hidden_size is None
                }
        return data

    def set_state(self, data):
        self.setText(data['text'])
        self.resize_to_content(data['text'].splitlines())
        if not data['shown']:
            self.hide()


class MatrixNode_MainWidget(MatrixWidget):
    def __init__(self, params):
        super().__init__(params, 100, 80)

        self.setReadOnly(False)
        self.textChanged.connect(self.text_changed)

    def text_changed(self):
        self.node.parse_matrix(self.toPlainText())
        self.resize_to_content(lines=self.toPlainText().splitlines())

    def focusOutEvent(self, e):
        self.update_matrix(self.node.expression_matrix)
        QTextEdit.focusOutEvent(self, e)


export_widgets(
    MatrixWidget,
    MatrixNode_MainWidget,
)
