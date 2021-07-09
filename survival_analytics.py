#################################### problem1 ###################################################
# pip install lifelines
import lifelines

import pandas as pd
# Loading dataset
patient_data = pd.read_csv("E:/DATA SCIENCE ASSIGNMENT/Class And Assignment Dataset/Asss/Survival Analytics/Patient.csv")
patient_data.head()
patient_data.describe()
patient_data.columns
patient_data["Followup"].describe()


#EDA
#Removing PatientID column
patient_data = patient_data.iloc[:,1:4]

#label enconding
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
patient_data['Scenario'] = label_encoder.fit_transform(patient_data['Scenario'])

# Followup is referring to time 
T = patient_data.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for Eventtype 
kmf.fit(T, event_observed=patient_data.Eventtype)

# Time-line estimations plot 
kmf.plot()

# Over Multiple Scenario 
# For each group, here group is Scenario
patient_data.Scenario.value_counts()

# Applying KaplanMeierFitter model on Time and Events for the Scenario "1"
kmf.fit(T[patient_data.Scenario==0], patient_data.Eventtype[patient_data.Scenario==0], label='1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and Events for the Scenario "0"
kmf.fit(T[patient_data.Scenario==0], patient_data.Eventtype[patient_data.Scenario==0], label='0')
kmf.plot(ax=ax)


############################################ problem2 ###############################################
# pip install lifelines
import lifelines

import pandas as pd
# Loading dataset
ECG_data = pd.read_excel("E:/DATA SCIENCE ASSIGNMENT/Class And Assignment Dataset/Asss/Survival Analytics/ECG_Surv.xlsx")
ECG_data.head()
ECG_data.describe()
ECG_data.columns
ECG_data["survival_time_hr"].describe()

#EDA
#Selecting required column
ECG_data = ECG_data[["survival_time_hr","alive","group"]]

# survival_time_hr is referring to time 
T = ECG_data.survival_time_hr

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for alive 
kmf.fit(T, event_observed=ECG_data.alive)

# Time-line estimations plot 
kmf.plot()

# Over Multiple group 
# For each group, here group is group
ECG_data.group.value_counts()

# Applying KaplanMeierFitter model on Time and Events for the group "1"
kmf.fit(T[ECG_data.group==1], ECG_data.alive[ECG_data.group==1], label='1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and Events for the group "0"
kmf.fit(T[ECG_data.group==1], ECG_data.alive[ECG_data.group==1], label='0')
kmf.plot(ax=ax)

#################################################### END #########################################

