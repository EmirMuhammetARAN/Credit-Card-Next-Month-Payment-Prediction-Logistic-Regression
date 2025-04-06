# Credit Card Next Month Payment Prediction using Logistic Regression

This project uses **Logistic Regression** to predict whether a customer will make a payment on their credit card next month, based on their financial and demographic data.

---

## Dataset

The dataset used is the [UCI Credit Card Default Dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients), which contains information about credit card clients, including payment status, bill statements, and demographic information.

**Total Samples:** 30000  
**Features Include:**  
- **Limit Balance** - Credit limit
- **Sex** - Gender
- **Education** - Education level
- **Marriage** - Marital status
- **Age** - Age of client
- **Previous Payment History**  
- And more...

**Target Variable:**  
- **`default.payment.next.month`** - Whether the client will make a payment (0) or not (1) next month.

---

## Model: Logistic Regression

The model is trained using the **Logistic Regression** algorithm to predict whether the customer will default or make the payment next month.

---

## How it Works

1. **Data Preprocessing:**  
   - `ID` column is dropped as it is not useful for prediction.
   - The target variable, `default.payment.next.month`, is separated from the feature columns.
   
2. **Train-Test Split:**  
   - The data is split into training (77%) and testing (23%) sets.
   
3. **Model Training:**  
   - Logistic Regression is applied to the training set.

4. **Prediction and Evaluation:**  
   - The model is evaluated using the test set and prediction accuracy is printed.

---

## Model Performance

```python
Model Accuracy: 0.77
