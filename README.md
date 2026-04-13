# vanilla_RNN-ML-5

# Palindrome Detection using Vanilla RNN

## Student Information
- Name: Sanaa Elattari
- Student ID: 21336359
- Email: sselattari@connect.ust.hk 

---

## Overview
This project implements a vanilla Recurrent Neural Network (RNN) with an embedding layer to classify whether a number (up to 7 digits) is a palindrome.

A palindrome reads the same forwards and backwards (e.g., 121, 1331, 12321).

---

## Model Architecture
- Input: Sequence of digits (0–9)
- Embedding size: 16
- Hidden size: 256
- Output: Binary classification (0 = not palindrome, 1 = palindrome)
- Activation: LogSoftmax
- Loss function: NLLLoss
- Optimization: Manual SGD

---

## Training Details

Three models were trained:

| Dataset Size | Epochs | Learning Rate |
|-------------|--------|---------------|
| 200         | 30     | 0.003         |
| 1000        | 30     | 0.003         |
| 50000       | 20     | 0.003         |

---

## Training Results

### Model (200 examples)
- Final Training Accuracy: ~0.78
- Test Accuracy: **0.548**

### Model (1000 examples)
- Final Training Accuracy: ~0.65
- Test Accuracy: **0.576**

### Model (50000 examples)
- Final Training Accuracy: ~0.56
- Test Accuracy: **0.574**

---

## Observations

- The model trained on 200 examples shows signs of overfitting.
- Increasing dataset size improves generalization slightly.
- However, performance saturates around ~57%.

This is because vanilla RNNs struggle with long-range dependencies required for palindrome detection.

---

## Training Logs

Training loss plots are included:
- loss_200.png
- loss_1000.png
- loss_50000.png

---

## Files Included

- main.py
- model_200.pth
- model_1000.pth
- model_50000.pth
- loss_200.png
- loss_1000.png
- loss_50000.png
- README.md

---

## How to Run

### 1. Train the models

Run:
python3 main.py

### 2. Evaluate on test.csv

To evaluate using the TA-provided test file:

Place `test.csv` in the same directory as `main.py`

Uncomment the following lines at the bottom of `main.py`:
run_on_csv("model_200.pth", "test.csv")
run_on_csv("model_1000.pth", "test.csv")
run_on_csv("model_50000.pth", "test.csv")

Run:
python3 main.py
