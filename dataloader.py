import pandas as pd 
uniliststring=["HKU", "CUHK", "HKUST"]

def read_data(enrolleduni):
    hkust = pd.read_excel("Data/HKUST Comp.xlsx").dropna().loc[:, ["Code","Title","Description"]]
    hku = pd.read_csv("Data/HKU Comp.csv").dropna()
    cuhk = pd.read_excel("Data/CUHK Comp.xlsx").dropna()
    
    unilistvariable=[hku, cuhk, hku]


    for (index,uni) in enumerate(unilistvariable):
        uni["University"]=uniliststring[index]
    match enrolleduni:
        case "HKUST":
            otheruni = pd.concat([hku,cuhk])
            myuni=hkust
        case "HKU":
            otheruni = pd.concat([hkust,cuhk])
            myuni=hku
        case "CUHK":
            otheruni = pd.concat([hkust,hku])
            myuni=cuhk
        case _:
            print("Sorry, we do not have data for the university you entered.")
            exit()
    otheruni = otheruni.drop_duplicates(subset=["Code"]).reset_index(drop=True)
    myunicourses=myuni["Code"].tolist()
    return myuni, myunicourses, otheruni

if __name__ == "__main__":
   ...
