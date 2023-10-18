 # Signals and Systems Laboratory Coursework


## Introduction
This lab will teach you some fundamentals of Digital Signal Processing (DSP), and introduce you to Python and Jupyter Notebooks, mathematical tools that integrate numerical analysis, matrix computation and graphics in an easy-to-use environment. Jupyter Notebooks are highly interactive; their interpretative nature allows you to explore mathematical concepts in signal processing without tedious programming. Once grasped, the same tool can be used for other subjects such as circuit analysis, communications, and control engineering.

## Learning Outcomes
At the end of this lab you will be able to:
1. Generate and analyse discrete-time signals using Python  
2. Analyse signals by applying Fourier transforms and window functions
3. Analyse digital filters and their responses
4. Demonstrate conceptual understanding of discrete signal processing 
5. Evaluate your work and your results

## Objectives
1. Derive equations for the 3 types of Discrete Fourier Transforms.
2. Generate sinusoidal signals in Python as vectors and investigate the effects of DFT and Windowing. You will then use these techniques to investigate an unknown signal (provided).
3. Filter noise from the unknown signal by removing unwanted frequencies in the frequency domain.
4. Investigate the effects of passing Pulse and Impulse signals through a digital filter.
5. Investigate simple digital filter and their responses (FIR and IIR).

## Requirements
To complete this lab you will need to install and run jupyter notebooks on you personal laptop.

## Recommended Textbooks
This experiment is designed to support the second year Signals and Systems course. While the notes provided in this experiment attempt to explain certain basic concepts, they are far from complete. You will likely find the recommended textbook helpful when studying this experiment as well as the lecture course: S. Haykin and B. Van Veen, 'Signals and Systems,' 2nd Ed., Wiley, 2003.


## Timetable
|Week starting|Lecture topic |Lab exercise |
|----|--------------|-------------|
|9/10|1: Introduction|/|
|16/10|2: LTI Systems|EX1 - Introduction|
|23/10|2: LTI Systems|EX2 - LTI systems|
|30/10|3: Sampling| EX3 - Sampling|
|6/11| Midterm| Midterm|
|13/11| 4: Fourier Transform| EX4 - Fourier|
|20/11| 5: Laplace | EX4 - Fourier|
|27/11| 6: z-Transform | EX5 - Filters|
|04/12| 7: Filters| EX6 - FIR/IIR Filters|


There are 6 exercises in this coursework, each relating to a topic covered in lectures. Each exercise should last approximately 2 hours. We strongly recommend that you attend scheduled lab sessions to work on this coursework. 


## Assessment
This coursework will be assessed as part of the exam. Normally, some of the parts of Question 1 of the exam will ask questions on the material covered in the coursework. The nominal weighting of the coursework-related questions in the exam amounts to 10% of the course total. Given that the material covered in the coursework is also covered in lectures and tutorial questions, coursework-related questions will not be labelled as such on the exam paper, and may be embedded in other questions. The coursework-related questions in the exam will specifically assess understanding of the theoretical concepts and the methods for signal analysis and processing covered in the coursework. The optional exercises in the coursework will not be assessed in the exam in a coursework-specific manner.

## Contact
This laboratory coursework was developed and designed by Aidan O. T. Hogg and Patrick A. Naylor (with help from Vincent W. Neo and Emilie d'Olne). Please post on the course Forum (or email p.naylor@imperial.ac.uk) if you have any suggestions or comments about this document as this will help future year groups.

# Getting started with Jupiter Notebooks

### Linux or MAC setup

**Video of setup:**

<p align="center">
<a href="https://www.youtube.com/watch?v=yxKV9jIBswU"><img src="/img/linux_video.png?raw=true" alt="Linux or MAC setup video"></a>
</p>

1. Download this Git repository 
2. Install Python 3.12 (or any version from 3.6 to 3.12) from <https://www.python.org/downloads/macos/>
3. Install the required Python packages 
```
python -m pip install numpy matplotlib scipy soundfile jupyter
```
__Note:__ you may need to replace ``python`` with ``python3``

4. Go to the `sap-EE2-SS-LAB` folder and run the Jupyter Notebook
```
python -m jupyter notebook
```
__Note:__ you may need to use ``python -m notebook`` instead
### Windows setup

**Video of setup:**

<p align="center">
<a href="https://www.youtube.com/watch?v=AVpcwfGi6D0"><img src="/img/windows_video.png?raw=true" alt="Windows setup video"></a>
</p>

1. Download this Git repository 
2. Install Python 3.12 (or any version from 3.6 to 3.12) from <https://www.python.org/downloads/>
3. Install the required Python packages 
```
python -m pip install numpy matplotlib scipy soundfile jupyter
```
4. Go to the `sap-EE2-SS-LAB` folder and run the Jupyter Notebook
```
jupyter notebook
```
__Note:__ you may need to use ``python -m notebook`` instead
