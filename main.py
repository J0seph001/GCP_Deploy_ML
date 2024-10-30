import numpy as np
from flask import Flask, request
from predict import make_prediction

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to my Flask API</h1>"
        "</body>"
        "</html>"
    )
    return body

@app.route("/predict", methods=["POST"])
def predict():
    data_json = request.get_json()
  
    NAME_CONTRACT_TYPE=data_json["NAME_CONTRACT_TYPE"]
    CODE_GENDER=data_json["CODE_GENDER"]
    CNT_CHILDREN=data_json["CNT_CHILDREN"]
    AMT_INCOME_TOTAL=data_json["AMT_INCOME_TOTAL"]
    AMT_CREDIT=data_json["AMT_CREDIT"]
    NAME_TYPE_SUITE=data_json["NAME_TYPE_SUITE"]
    NAME_INCOME_TYPE=data_json["NAME_INCOME_TYPE"]
    NAME_EDUCATION_TYPE=data_json["NAME_EDUCATION_TYPE"]
    NAME_FAMILY_STATUS=data_json["NAME_FAMILY_STATUS"]
    NAME_HOUSING_TYPE=data_json["NAME_HOUSING_TYPE"]
    REGION_POPULATION_RELATIVE=data_json["REGION_POPULATION_RELATIVE"]
    DAYS_EMPLOYED=data_json["DAYS_EMPLOYED"]
    DAYS_REGISTRATION=data_json["DAYS_REGISTRATION"]
    DAYS_ID_PUBLISH=data_json["DAYS_ID_PUBLISH"]
    OCCUPATION_TYPE=data_json["OCCUPATION_TYPE"]
    REGION_RATING_CLIENT_W_CITY=data_json["REGION_RATING_CLIENT_W_CITY"]
    LIVE_REGION_NOT_WORK_REGION=data_json["LIVE_REGION_NOT_WORK_REGION"]
    REG_CITY_NOT_WORK_CITY=data_json["REG_CITY_NOT_WORK_CITY"]
    ORGANIZATION_TYPE=data_json["ORGANIZATION_TYPE"]
    EXT_SOURCE_2=data_json["EXT_SOURCE_2"]
    EXT_SOURCE_3=data_json["EXT_SOURCE_3"]
    OBS_30_CNT_SOCIAL_CIRCLE=data_json["OBS_30_CNT_SOCIAL_CIRCLE"]
    DEF_30_CNT_SOCIAL_CIRCLE=data_json["DEF_30_CNT_SOCIAL_CIRCLE"]
    AMT_REQ_CREDIT_BUREAU_WEEK=data_json["AMT_REQ_CREDIT_BUREAU_WEEK"]
    AMT_REQ_CREDIT_BUREAU_QRT=data_json["AMT_REQ_CREDIT_BUREAU_QRT"]
    FLAG_OWN_CAR=data_json["FLAG_OWN_CAR"]
    FLAG_OWN_REALTY=data_json["FLAG_OWN_REALTY"]
    AGE=data_json["AGE"]
    YEARS_LAST_PHONE_CHANGE=data_json["YEARS_LAST_PHONE_CHANGE"]

    DIV_AMT_INCOME_TOTAL_AMT_CREDIT=data_json["AMT_INCOME_TOTAL/AMT_CREDIT"]

    bad_debt_count=data_json["bad_debt_count"]
    AMT_CREDIT_SUM_DEBT=data_json["AMT_CREDIT_SUM_DEBT"]
    AMT_CREDIT_SUM=data_json["AMT_CREDIT_SUM"]
    avg_late_payments=data_json["avg_late_payments"]
    rejected_for_loan_count=data_json["rejected_for_loan_count"]
    conseq_neg_cred_card_balance=data_json["conseq_neg_cred_card_balance"]
    extended_cred_card_debt=data_json["extended_cred_card_debt"]


    data = np.array([[
        NAME_CONTRACT_TYPE,
        CODE_GENDER,
        CNT_CHILDREN,
        AMT_INCOME_TOTAL,
        AMT_CREDIT,
        NAME_TYPE_SUITE,
        NAME_INCOME_TYPE,
        NAME_EDUCATION_TYPE,
        NAME_FAMILY_STATUS,
        NAME_HOUSING_TYPE,
        REGION_POPULATION_RELATIVE,
        DAYS_EMPLOYED,
        DAYS_REGISTRATION,
        DAYS_ID_PUBLISH,
        OCCUPATION_TYPE,
        REGION_RATING_CLIENT_W_CITY,
        LIVE_REGION_NOT_WORK_REGION,
        REG_CITY_NOT_WORK_CITY,
        ORGANIZATION_TYPE,
        EXT_SOURCE_2,
        EXT_SOURCE_3,
        OBS_30_CNT_SOCIAL_CIRCLE,
        DEF_30_CNT_SOCIAL_CIRCLE,
        AMT_REQ_CREDIT_BUREAU_WEEK,
        AMT_REQ_CREDIT_BUREAU_QRT,
        FLAG_OWN_CAR,
        FLAG_OWN_REALTY,
        AGE,
        YEARS_LAST_PHONE_CHANGE,

        DIV_AMT_INCOME_TOTAL_AMT_CREDIT,
        
        bad_debt_count,
        AMT_CREDIT_SUM_DEBT,
        AMT_CREDIT_SUM,
        avg_late_payments,
        rejected_for_loan_count,
        conseq_neg_cred_card_balance,
        extended_cred_card_debt
        ]])


    predictions = make_prediction(data)
  
    return str(predictions)

if __name__ == "__main__":
    app.run()