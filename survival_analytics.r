############################## problem1 #######################################
# Survival Analysis in R
library(readr)
install.packages('survminer')
install.packages("survival")

library(survminer)
library(survival)


patient_data <- read.csv("E:\\DATA SCIENCE ASSIGNMENT\\Class And Assignment Dataset\\Asss\\Survival Analytics\\Patient.csv",stringsAsFactors = TRUE)

attach(patient_data)
str(patient_data)

#EDA
patient_data <- patient_data[,c(2,3,4)]
str(patient_data)
colnames(patient_data)
# Define variables 
time <- Followup
event <- Eventtype
group <- Scenario  # unemployment insurance can take 2 values 0 or 1 

# Descriptive statistics
summary(time)
table(event)
table(group)

# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, event) ~ 1)

summary(kmsurvival)

plot(kmsurvival, xlab="Time", ylab="Survival Probability")

ggsurvplot(kmsurvival, data=patient_data, risk.table = TRUE)


# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)

plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=survival_unemployment1, risk.table = TRUE)

############################# problem2 ##########################################
# Survival Analysis in R
library(readr)
install.packages('survminer')
install.packages("survival")

library(survminer)
library(survival)


ECG_data <- readxl::read_excel("E:\\DATA SCIENCE ASSIGNMENT\\Class And Assignment Dataset\\Asss\\Survival Analytics\\ECG_Surv.xlsx")

attach(ECG_data)
str(ECG_data)

#EDA
ECG_data <- ECG_data[,c(1,2,12)]
str(ECG_data)
colnames(ECG_data)
# Define variables 
time <- survival_time_hr
event <- alive
group <- group  # unemployment insurance can take 2 values 0 or 1 

# Descriptive statistics
summary(time)
table(event)
table(group)

# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, event) ~ 1)

summary(kmsurvival)

plot(kmsurvival, xlab="Time", ylab="Survival Probability")

ggsurvplot(kmsurvival, data=ECG_data, risk.table = TRUE)


# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)

plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=ECG_data, risk.table = TRUE)
############################## END ############################################