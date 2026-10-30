"""
NISR 2026 Big Data Hackathon - Agricultural Productivity Pipeline
Module: Model Architecture, Placeholder Execution, and TensorBoard Tracking
Authors: Inyange Analytics (Kevin Nizeyimana & Laura Kwizera Karangwa)
"""

import os
import time
import numpy as np
from tensorboardX import SummaryWriter

class TabularGradientBoostingRegressor:
    """
    Lightweight, dependency-free Gradient Boosted Decision Tree regressor
    designed for tabular survey features with support for step-wise
    iterative placeholder execution and TensorBoard metric logging.
    """
    def __init__(self, n_estimators: int = 1, learning_rate: float = 0.05, max_depth: int = 3, l2_reg: float = 1e-3, random_state: int = 42):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.l2_reg = l2_reg
        self.random_state = random_state
        self.weights = None
        self.bias = None
        self.base_pred = None

    def fit_placeholder_step(self, X: np.ndarray, y: np.ndarray):
        """
        Executes a single placeholder estimation step (1 iteration / 1 estimator pass).
        Fits a regularized linear-ridge residual base learner to verify gradient flow
        and end-to-end tensor transformations.
        """
        np.random.seed(self.random_state)
        n_samples, n_features = X.shape
        self.base_pred = np.mean(y)
        residuals = y - self.base_pred
        
        # Ridge closed-form solution on initial residual: (X^T X + lambda I)^(-1) X^T residuals
        eye = np.eye(n_features, dtype=np.float32) * self.l2_reg
        XtX = np.dot(X.T, X) + eye
        Xtr = np.dot(X.T, residuals)
        self.weights = np.linalg.solve(XtX, Xtr)
        self.bias = np.mean(residuals - np.dot(X, self.weights))
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.weights is None:
            raise ValueError("Model has not been fitted.")
        return self.base_pred + self.learning_rate * (np.dot(X, self.weights) + self.bias)

def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray):
    """
    Computes standard regression evaluation metrics: MSE, MAE, RMSE, and R-squared.
    """
    mse = float(np.mean((y_true - y_pred) ** 2))
    mae = float(np.mean(np.abs(y_true - y_pred)))
    rmse = float(np.sqrt(mse))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    r2 = float(1.0 - (ss_res / (ss_tot + 1e-8)))
    return {"mse": mse, "mae": mae, "rmse": rmse, "r2": r2}

def run_placeholder_pipeline(X_train: np.ndarray, X_val: np.ndarray, y_train: np.ndarray, y_val: np.ndarray, log_dir: str = "logs/placeholder_run"):
    """
    Executes a single placeholder pass (1 iteration) verifying pipeline execution end-to-end.
    Logs scalar performance metrics, model architecture summary, and hyperparameters to TensorBoard.
    """
    os.makedirs(log_dir, exist_ok=True)
    writer = SummaryWriter(log_dir=log_dir)
    
    print("=" * 70)
    print("STARTING PLACEHOLDER RUN (1 ITERATION / 1 ESTIMATOR PASS)")
    print("=" * 70)
    
    # 1. Model initialization
    hyperparams = {
        "n_estimators": 1,
        "learning_rate": 0.05,
        "max_depth": 3,
        "l2_reg": 1e-3,
        "model_type": "GradientBoosting_Tabular_Baseline"
    }
    model = TabularGradientBoostingRegressor(**{k: v for k, v in hyperparams.items() if k != "model_type"})
    
    # 2. Single-step placeholder fitting
    start_time = time.time()
    model.fit_placeholder_step(X_train, y_train)
    fit_duration = time.time() - start_time
    
    # 3. Model predictions
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)
    
    # 4. Metric computation
    train_metrics = compute_metrics(y_train, y_train_pred)
    val_metrics = compute_metrics(y_val, y_val_pred)
    
    print(f"Placeholder run completed in {fit_duration:.4f}s")
    print(f"Train MSE: {train_metrics['mse']:.4f} | Train MAE: {train_metrics['mae']:.4f} | Train R2: {train_metrics['r2']:.4f}")
    print(f"Val MSE:   {val_metrics['mse']:.4f} | Val MAE:   {val_metrics['mae']:.4f} | Val R2:   {val_metrics['r2']:.4f}")
    
    # 5. TensorBoard Logging - Step 1 Scalars
    step = 1
    writer.add_scalar("loss/train_mse", train_metrics["mse"], global_step=step)
    writer.add_scalar("loss/val_mse", val_metrics["mse"], global_step=step)
    writer.add_scalar("metrics/train_mae", train_metrics["mae"], global_step=step)
    writer.add_scalar("metrics/val_mae", val_metrics["mae"], global_step=step)
    writer.add_scalar("metrics/train_rmse", train_metrics["rmse"], global_step=step)
    writer.add_scalar("metrics/val_rmse", val_metrics["rmse"], global_step=step)
    writer.add_scalar("metrics/val_r2", val_metrics["r2"], global_step=step)
    
    # 6. TensorBoard Logging - Model Graph & Architecture Text Description
    arch_description = f"""
    ### Model Architecture: GRADIENT BOOSTING TABULAR REGRESSOR
    - **Target Variable**: Post-Harvest Loss Percentage (%)
    - **Estimators (Current Placeholder)**: {hyperparams['n_estimators']}
    - **Learning Rate**: {hyperparams['learning_rate']}
    - **Max Tree Depth**: {hyperparams['max_depth']}
    - **L2 Weight Regularization**: {hyperparams['l2_reg']}
    - **Input Feature Dimension**: {X_train.shape[1]} features (One-Hot Encoded & Scaled)
    - **Execution Mode**: End-to-end verification pass (Not fully trained)
    """
    writer.add_text("model/architecture_summary", arch_description, global_step=step)
    
    # 7. TensorBoard Logging - Hyperparameters (HParams)
    hparam_dict = {
        "model_type": hyperparams["model_type"],
        "n_estimators": hyperparams["n_estimators"],
        "learning_rate": hyperparams["learning_rate"],
        "l2_reg": hyperparams["l2_reg"]
    }
    metric_dict = {
        "hparam/val_mse": val_metrics["mse"],
        "hparam/val_mae": val_metrics["mae"],
        "hparam/val_r2": val_metrics["r2"]
    }
    writer.add_hparams(hparam_dict=hparam_dict, metric_dict=metric_dict)
    
    writer.flush()
    writer.close()
    
    print(f"\n[TensorBoard] Successfully logged scalars, architecture, and HParams to '{log_dir}'")
    
    return {
        "model": model,
        "train_metrics": train_metrics,
        "val_metrics": val_metrics,
        "hyperparams": hyperparams,
        "log_dir": log_dir
    }
