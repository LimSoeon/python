from fastapi import FastAPI
import pandas as pd
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data/{sheetName}")
async def getData(sheetName):
    file_name = './data/features.xlsx'        
    originalDataFile = pd.read_excel(file_name,sheet_name=sheetName)

    resultList = []
    for index, row in originalDataFile.iterrows():
        result = {
            "No" : index,
            "words" : row['word'],
            "mean" : row['mean'],
            "englishSentence" : row["englishSentence"],
            "koreanSentence" : row["koreanSentence"]
        }
        resultList.append(result); 
    print(resultList)
    return resultList;

@app.get("/word/{sheetName}")
async def word (sheetName):
    df = pd.read_excel('data/features.xlsx', sheet_name=sheetName)
    randomnumber = random.randrange(0, len(df.columns)+1)
    word_db = { 
        "keyword": df.loc[randomnumber].keyword,
        "word_mean": df.loc[randomnumber].word_mean,
        "englishSentence" : df.loc[randomnumber].englishSentence,
        "koreanSentence": df.loc[randomnumber].koreanSentence,
    }
    return word_db