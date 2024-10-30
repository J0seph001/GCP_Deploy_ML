import joblib
import pandas as pd

model = joblib.load("model.pkl")

def make_prediction(inputs):
    """
    Make a prediction using the trained model
    """
    inputs_df = pd.DataFrame(
        inputs,
        columns=[
            "NAME_CONTRACT_TYPE",
            "CODE_GENDER",
            "CNT_CHILDREN",
            "AMT_INCOME_TOTAL",
            "AMT_CREDIT",
            "NAME_TYPE_SUITE",
            "NAME_INCOME_TYPE",
            "NAME_EDUCATION_TYPE",
            "NAME_FAMILY_STATUS",
            "NAME_HOUSING_TYPE",
            "REGION_POPULATION_RELATIVE",
            "DAYS_EMPLOYED",
            "DAYS_REGISTRATION",
            "DAYS_ID_PUBLISH",
            "OCCUPATION_TYPE",
            "REGION_RATING_CLIENT_W_CITY",
            "LIVE_REGION_NOT_WORK_REGION",
            "REG_CITY_NOT_WORK_CITY",
            "ORGANIZATION_TYPE",
            "EXT_SOURCE_2",
            "EXT_SOURCE_3",
            "OBS_30_CNT_SOCIAL_CIRCLE",
            "DEF_30_CNT_SOCIAL_CIRCLE",
            "AMT_REQ_CREDIT_BUREAU_WEEK",
            "AMT_REQ_CREDIT_BUREAU_QRT",
            "FLAG_OWN_CAR",
            "FLAG_OWN_REALTY",
            "AGE",
            "YEARS_LAST_PHONE_CHANGE",

            "DIV_AMT_INCOME_TOTAL_AMT_CREDIT",

            "bad_debt_count",
            "AMT_CREDIT_SUM_DEBT",
            "AMT_CREDIT_SUM",
            "avg_late_payments",
            "rejected_for_loan_count",
            "conseq_neg_cred_card_balance",
            "extended_cred_card_debt"
            ]
        )
    predictions = model.predict(inputs_df)
  
    return predictions