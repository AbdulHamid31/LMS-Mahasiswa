
import pickle
import pandas as pd

with open("models/model_xgb.pkl", "rb") as f:
    model = pickle.load(f)
with open("models/explainer_shap.pkl", "rb") as f:
    explainer = pickle.load(f)

def predict_dropout(data: pd.DataFrame):
    pred_prob = model.predict_proba(data)[0][1]
    pred_label = int(pred_prob >= 0.5)
    shap_values = explainer(data)
    return pred_label, pred_prob, shap_values.values, data
