from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt
import sys
from main import parse_equation

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Chemical Equation Balancer")
window.setMinimumSize(900, 700)

layout = QGridLayout()
window.setLayout(layout)

def make_box(widget):
    frame = QFrame()
    frame.setFrameShape(QFrame.Shape.StyledPanel)
    frame.setStyleSheet("border: 2px solid #aaa; border-radius: 24px; padding: 4px;")
    inner = QVBoxLayout()
    inner.setContentsMargins(5, 5, 5, 5)
    inner.addWidget(widget)
    frame.setLayout(inner)
    return frame

input_field = QLineEdit()
input_field.setPlaceholderText("Enter chemical equation like: Mg(CO^2) = Mg + C + O^2")
input_field.setStyleSheet("font-size: 16px; padding: 6px;")
input_field.setFixedHeight(40)

matrix_label = QLabel("Matrix Output")
matrix_label.setWordWrap(True)
matrix_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

element_label = QLabel("Element Count")
element_label.setWordWrap(True)
element_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

result_label = QLabel("Result")
result_label.setWordWrap(True)
result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

matrix_label.setStyleSheet("border: none; background: transparent; font-size: 14px;")
element_label.setStyleSheet("border: none; background: transparent; font-size: 14px;")
result_label.setStyleSheet("border: none; background: transparent; font-size: 24px;")

layout.addWidget(make_box(input_field), 0, 0, 1, 2)
layout.addWidget(make_box(matrix_label), 1, 0)
layout.addWidget(make_box(element_label), 1, 1)
layout.addWidget(make_box(result_label), 2, 0, 1, 2)

def on_submit():
    eq = input_field.text()
    _, matrix, balanced, elements = parse_equation(eq)
    matrix_label.setText(matrix if matrix else "Check Your Equation")
    result_label.setText(balanced if balanced else "Can't Balance (Check Your Equation)")
    element_label.setText(elements if elements else "Check Your Equation")

input_field.returnPressed.connect(on_submit)

window.show()
sys.exit(app.exec())
