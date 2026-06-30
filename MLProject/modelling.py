import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier

def train():
    with mlflow.start_run() as run:
        print("Membaca dataset...")
        train_df = pd.read_csv("telco_preprocessing/train.csv")
        
        X_train = train_df.drop('Churn', axis=1)
        y_train = train_df['Churn']
        
        print("Melatih model Random Forest...")
        rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        rf.fit(X_train, y_train)
        
        print("Menyimpan model ke artifact...")
        mlflow.sklearn.log_model(rf, "model")
        
        # Simpan Run ID ke file teks untuk Docker Build
        with open("run_id.txt", "w") as f:
            f.write(run.info.run_id)
        
        print("Selesai! Run ID berhasil dicatat.")

if __name__ == "__main__":
    train()