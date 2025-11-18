import logging
import pandas as pd

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler("data.log")
file_handler.setLevel(logging.DEBUG)

consoler=logging.StreamHandler()
consoler.setLevel(logging.DEBUG)

formater=logging.Formatter("%(asctime)s-%(lineno)d-%(message)s-%(levelno)s")

file_handler.setFormatter(formater)
consoler.setFormatter(formater)

logger.addHandler(file_handler)
logger.addHandler(consoler)
logger.debug("logger init")

def loader (path):
    try:
        df=pd.read_csv(path)
        logger.debug("csv file loaded")
        return df
    except Exception as e:
        logger.error(e)

def age_modifer(df):
    try:
        def pre (x):
            try:
                val=int(x)
                return val
            except:
                return 0
        df["age"]=df["age"].map(pre)
        df=df[df["age"]>6]
        logger.debug("age column done")
        return df
    except Exception as e:
        logger.error(e)
def marks_modifer(df):
    try:
        def pre (x):
            try:
                val=int(x)
                return val
            except:
                return 0
        df["marks"]=df["marks"].map(pre)
        return df
    except Exception as e:
        logger.error(e)
def main():
    logger.debug("program started")
    path="data\students.csv"
    df=loader(path)
    logger.debug("file loaded")
    df=age_modifer(df)
    logger.debug("preprocessing done for age")
    df=marks_modifer(df)
    logger.debug("preprocessing done for marks")
    try:
        df.to_csv("students_raw.csv", index=False)
        logger.debug("csv saved")
    except Exception as e:
        logger.error(e)
main()