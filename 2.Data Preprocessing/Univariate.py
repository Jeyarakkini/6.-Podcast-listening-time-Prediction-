import pandas as pd
class Univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)        
        return quan,qual
    def descriptive(dataset,quan):
        descriptive=pd.DataFrame(index=['Max','Min','Mean','Median','Mode','Q1:25%','Q2:50%','Q3:75%','Q4:100%','IQR',
                                                '1.5IQR','lesserRange','greaterRange'],columns=quan)
        for columnName in quan:
            descriptive[columnName]['Max']=dataset.describe()[columnName]['max']
            descriptive[columnName]['Min']=dataset.describe()[columnName]['min']
            descriptive[columnName]['Mean']=dataset[columnName].mean()
            descriptive[columnName]['Median']=dataset[columnName].median()
            descriptive[columnName]['Mode']=dataset[columnName].mode()[0]
            descriptive[columnName]['Q1:25%']=dataset.describe()[columnName]['25%']
            descriptive[columnName]['Q2:50%']=dataset.describe()[columnName]['50%']
            descriptive[columnName]['Q3:75%']=dataset.describe()[columnName]['75%']
            descriptive[columnName]['Q4:100%']=dataset.describe()[columnName]["max"]
            descriptive[columnName]['IQR']=descriptive[columnName]['Q3:75%']-descriptive[columnName]['Q1:25%']
            descriptive[columnName]['1.5IQR']=1.5*descriptive[columnName]['IQR']
            descriptive[columnName]['lesserRange']=descriptive[columnName]['Q1:25%']-descriptive[columnName]['1.5IQR']
            descriptive[columnName]['greaterRange']=descriptive[columnName]['Q3:75%']+descriptive[columnName]['1.5IQR']
            descriptive
        return descriptive
    def findOutlier(descriptive,quan):
        lesser=[]
        greater=[]
        for columnName in quan:
            if(descriptive[columnName]["lesserRange"]>descriptive[columnName]["Min"]):
                lesser.append(columnName)
            if(descriptive[columnName]["greaterRange"]<descriptive[columnName]['Max']):
                greater.append(columnName)
        return lesser,greater
    def replaceOutlier(dataset,descriptive,lesser,greater,quan):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]['lesserRange']]=descriptive[columnName]['lesserRange']
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]['greaterRange']]=descriptive[columnName]['greaterRange']
        return dataset            
        
    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=['unique_values','frequency','relative_frequency','cumsum'])
        freqTable['unique_values']=dataset[columnName].value_counts().index
        freqTable['frequency']=dataset[columnName].value_counts().values
        freqTable['relative_frequency']=freqTable['frequency']/freqTable['unique_values'].count()
        freqTable['cumsum']=freqTable['relative_frequency'].cumsum()
        return freqTable
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                          