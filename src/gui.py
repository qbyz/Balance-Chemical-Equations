import time
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QVBoxLayout, QFrame, QPushButton, QSlider
from PyQt6.QtCore import Qt
import sys
from main import parse_equation
import random

equations = [
    'H^2 + O^2 = H^2O',
    'Na + Cl^2 = NaCl',
    'Mg + O^2 = MgO',
    'Fe + O^2 = Fe^2O^3',
    'C + O^2 = CO^2',
    'Ca(OH)^2 + HCl = CaCl^2 + H^2O',
    'Al + HCl = AlCl^3 + H^2',
    'Na^3 PO^4 + Ba(NO^3)^2 = Ba^3 (PO^4)^2 + NaNO^3',
    'KOH + H^2 SO^4 = K^2 SO^4 + H^2O',
    'Mg + HNO^3 = Mg(NO^3)^2 + H^2',
    'Zn + H^2 SO^4 = Zn SO^4 + H^2',
    'Cu + HNO^3 = Cu(NO^3)^2 + NO + H^2O',
    'CaCO^3 + HCl = CaCl^2 + CO^2 + H^2O',
    'NaOH + H^3PO^4 = Na^3PO^4 + H^2O',
    'Al^2(SO^4)^3 + NaOH = Al(OH)^3 + Na^2SO^4',
    'C^2H^6 + O^2 = CO^2 + H^2O',
    'C^6H^12O^6 + O^2 = CO^2 + H^2',
    'Fe^2(SO^4)^3 + KOH = K^2SO^4 + Fe(OH)^3',
    'NH^3 + O^2 = NO + H^2O',
    'P^4 + O^2 = P^2O^5',
    'Cr^2(SO^4)^3 + KOH = K^2SO^4 + Cr(OH)^3',
    'K^4Fe(CN)^6 + KMnO^4 + H^2SO^4 = Fe^2(SO^4)^3 + MnSO^4 + K^2SO^4 + H^2O + CO^2 + NO'
]

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Chemical Equation Balancer")
window.setMinimumSize(900, 700)

layout = QGridLayout()
window.setLayout(layout)

def make_box(widget, maxwidth=None):
    frame = QFrame()
    frame.setFrameShape(QFrame.Shape.StyledPanel)
    frame.setStyleSheet("border: 2px solid #aaa; border-radius: 24px; padding: 4px;")
    if maxwidth:
        frame.setMaximumWidth(maxwidth)
    inner = QVBoxLayout()
    inner.setContentsMargins(5, 5, 5, 5)
    inner.addWidget(widget)
    frame.setLayout(inner)
    return frame

solveMode = QPushButton("Solve Only")
raceMode = QPushButton("Race Mode")

raceMode.setStyleSheet("padding: 200px; font-size: 20px;")
solveMode.setStyleSheet("padding: 200px; font-size: 20px;")

layout.addWidget(raceMode, 3, 1, 3, 1)
layout.addWidget(solveMode, 3, 0, 3, 1)

def race():
    solveMode.deleteLater()
    raceMode.deleteLater()

    equation = QLabel()
    equation.setText("Equation Will Appear Here")
    equation.setStyleSheet("font-size: 16px; padding: 6px;")
    equation.setFixedHeight(40)

    startButton = QPushButton("Start")
    startButton.setStyleSheet("padding: 10px; font-size: 20px; height: 175px;")

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

    userAnswer = QLineEdit()
    userAnswer.setPlaceholderText("Enter Your Answer (Just Digits e.g., '1,1,1,1')")

    headStart_label = QLabel()
    headStart_slider = QSlider(Qt.Orientation.Horizontal)

    headStart_label.setStyleSheet("border:none;")
    headStart_slider.setStyleSheet("border:none;")
    headStart_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    headStart_slider.setRange(0, 20)
    headStart_slider.setValue(0)
    headStart_label.setText('Head Start: 0 Seconds')
    headStart_slider.setMaximumWidth(300)

    sliderLayout = QVBoxLayout()
    sliderLayout.addWidget(headStart_label)
    sliderLayout.addWidget(headStart_slider, alignment=Qt.AlignmentFlag.AlignCenter)

    sliderWidget = QWidget()
    sliderWidget.setStyleSheet("border:none;")
    sliderWidget.setLayout(sliderLayout)

    layout.addWidget(make_box(sliderWidget, maxwidth=300), 0, 3)
    layout.addWidget(startButton, 0, 0)
    layout.addWidget(make_box(userAnswer), 2, 2, 1, 2)
    layout.addWidget(make_box(equation), 0, 1, 1, 2)
    layout.addWidget(make_box(matrix_label), 1, 0, 1, 2)
    layout.addWidget(make_box(element_label), 1, 2, 1, 2)
    layout.addWidget(make_box(result_label), 2, 0, 1, 2)

    startTime = time.time()
    endTime = time.time()
    eq = ''
    coeffs = []
    runTime = 0
    balanced = ''
    elements = ''
    matrix = []
    delay = 0

    def updateSliderLabel(value):
        nonlocal delay
        delay = value
        headStart_label.setText(f'Head Start: {value} Seconds')

    headStart_slider.valueChanged.connect(updateSliderLabel)

    def on_eq_submit():
        nonlocal runTime, coeffs, balanced, elements, eq, matrix
        equation.setText(equations[random.randint(0, len(equations)-1)])
        eq = equation.text()
        _, matrix, balanced, elements, runTime, coeffs = parse_equation(eq, True)
        print(coeffs)
        nonlocal startTime
        startTime = time.time()+delay

    def on_answer_submit():
        answer = userAnswer.text()
        print(answer)
        answer = [int(x) for x in answer.split(',')]  # Convert to integers
        print(answer)
        print(coeffs)
        if answer == coeffs:
            nonlocal endTime
            endTime = time.time()
            userSolveTime = endTime-startTime
            if userSolveTime > runTime:
                result_label.setText(f'Correct (But you Lost)\nYour Time: {userSolveTime} Seconds\nComputer Time: {runTime} Seconds')
                matrix_label.setText(matrix if matrix else "Check Your Equation")
                element_label.setText(elements if elements else "Check Your Equation")
            else:
                result_label.setText(f"Correct (YOU WON!!!)\nTime: {userSolveTime} Seconds!\nComputer Time: {runTime} Seconds")
                matrix_label.setText(matrix if matrix else "Check Your Equation")
                element_label.setText(elements if elements else "Check Your Equation")
        else:
            result_label.setText("Incorrect, try again (Time's Still Running).")


    startButton.clicked.connect(on_eq_submit)
    userAnswer.returnPressed.connect(on_answer_submit)

def solve():
    solveMode.deleteLater()
    raceMode.deleteLater()

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
        _, matrix, balanced, elements, runTime, coeffs = parse_equation(eq, False)
        matrix_label.setText(matrix if matrix else "Check Your Equation")
        result_label.setText(balanced if balanced else "Can't Balance (Check Your Equation)")
        element_label.setText(elements if elements else "Check Your Equation")

    input_field.returnPressed.connect(on_submit)

solveMode.clicked.connect(solve)
raceMode.clicked.connect(race)

window.show()
sys.exit(app.exec())
