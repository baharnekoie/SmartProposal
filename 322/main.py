# xai_user_trust_test_with_libs.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import shap


def get_score(question):
    while True:
        try:
            score = int(input(question))
            if 1 <= score <= 5:
                return score
            else:
                print("Lotfan adadi beyn 1 ta 5 vared konid.")
        except ValueError:
            print("Voroodi namo'tabar ast. Adad vared konid.")


def train_simple_model():
    """
    Sakht va train yek model sade
    """
    data = {
        "income": [20000, 40000, 60000, 80000],
        "debt": [15000, 10000, 5000, 2000],
        "credit": [0.3, 0.6, 0.8, 0.9],
        "label": [0, 0, 1, 1]
    }

    df = pd.DataFrame(data)
    X = df[["income", "debt", "credit"]]
    y = df["label"]

    model = LogisticRegression()
    model.fit(X, y)

    return model, X


def show_model_output(model, sample):
    pred = model.predict(sample)[0]
    decision = "Loan Approved" if pred == 1 else "Loan Rejected"

    print("\nModel Output:")
    print(f"Decision: {decision}")


def show_xai_explanation(model, X, sample):
    print("\nXAI Explanation (feature importance):")

    explainer = shap.LinearExplainer(model, X)
    shap_values = explainer.shap_values(sample)

    for feature, value in zip(sample.columns, shap_values[0]):
        percent = round(abs(value) * 100, 2)
        print(f"- {feature}: {percent}%")


def main():
    print("XAI User Trust Evaluation")
    print("-" * 40)

    model, X_train = train_simple_model()

    user_sample = pd.DataFrame({
        "income": [30000],
        "debt": [12000],
        "credit": [0.4]
    })

    show_model_output(model, user_sample)

    trust_before = get_score(
        "\nMizan etemad shoma be model ghabl az didan tozihat (1 ta 5): "
    )

    show_xai_explanation(model, X_train, user_sample)

    trust_after = get_score(
        "\nMizan etemad shoma be model bad az didan tozihat (1 ta 5): "
    )

    diff = trust_after - trust_before

    print("\nEvaluation Result")
    print("-" * 40)
    print(f"Etemad ghabl az tozih: {trust_before}")
    print(f"Etemad bad az tozih: {trust_after}")

    if diff > 0:
        print(f"Etemad karbar {diff} vahed afzayesh yafte ast.")
    elif diff < 0:
        print(f"Etemad karbar {-diff} vahed kahesh yafte ast.")
    else:
        print("Etemad karbar taghiri nakarde ast.")


if __name__ == "__main__":
    main()
