import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load model yang sudah disimpan
model = joblib.load('model_attrition.pkl')

# LabelEncoder yang digunakan saat training (jika perlu, bisa disimpan dan diload juga)
le = LabelEncoder()
le.fit(["Yes", "No"])  # Contoh untuk fitur biner seperti Attrition, bisa disesuaikan

def predict_attrition(new_data: pd.DataFrame):
    """
    new_data: DataFrame dengan fitur yang sudah diproses (encoding dll.)
    """
    prediction = model.predict(new_data)
    probability = model.predict_proba(new_data)

    return prediction, probability


data_baru = pd.DataFrame([{
    'EmployeeId': 731.5,
    'Age': 36.0,
    'BusinessTravel': 2.0,
    'DailyRate': 817.5,
    'Department': 1.0,
    'DistanceFromHome': 7.0,
    'Education': 3.0,
    'EducationField': 2.0,
    'EmployeeCount': 1.0,
    'EnvironmentSatisfaction': 3.0,
    'Gender': 1.0,
    'HourlyRate': 66.0,
    'JobInvolvement': 3.0,
    'JobLevel': 2.0,
    'JobRole': 4.0,
    'JobSatisfaction': 3.0,
    'MaritalStatus': 1.0,
    'MonthlyIncome': 5772.0,
    'MonthlyRate': 14235.5,
    'NumCompaniesWorked': 2.0,
    'Over18': 1.0, 
    'OverTime': 0.0,
    'PercentSalaryHike': 14.0,
    'PerformanceRating': 3.0,
    'RelationshipSatisfaction': 3.0,
    'StandardHours': 80.0,
    'StockOptionLevel': 0.0,
    'TotalWorkingYears': 14.0,
    'TrainingTimesLastYear': 2.0,
    'WorkLifeBalance': 3.0,
    'YearsAtCompany': 5.0,
    'YearsInCurrentRole': 3.0,
    'YearsSinceLastPromotion': 1.0,
    'YearsWithCurrManager': 3.0,
    'YearsUntilRetirement': 24.0,
    'WorkingYearsRatio': 0.636364,
    'IncomePerLevel': 2886.0,
    'TenureGroup': 2.0,
}])

# Prediksi
prediksi, probabilitas = predict_attrition(data_baru)
print("Prediksi (0: Tidak keluar, 1: Keluar):", prediksi[0])
print("Probabilitas Keluar:", round(probabilitas[0][1]*100, 2), "%")
