# Azure-Data-Platform
Technology - Azure Data Engineering Stack; Domain - Healthcare Revenue Cycle Management (RCM)

RCM is the process that hospitals use to manage the financial aspects, from the time the patient schedules an appointment till the time the provider gets paid. Here is a simplified breakdown:
1.It starts with a patient visit: patient details and insurance details are collected by the hospital or clinic. This ensure the provider knows who will pay for the services, insurance, the patient, or both will pay for it.
2. Services are provided.
3. Billing happens: The hospital will create a bill.
4. Claims are reviewed: Insurance company will review the bill. It might accept it, pay in full or partial or decline.
5. Payments and follow-ups. If partial payment is done by insurance company, then some portion is given by the patient, and the provider will follow up for the payment.
6. Tracking and improvement. The hospital will monitor the process.

RCM ensures the hospital can provide quality care while also staying financially healthy. 

As part of RCM we have 2 main aspects: 
- Accounts Receivable (AR): The money the provides receive.  https://mdmanagementgroup.com/healthcare-accounts-receivable-management/
- Accounts Payable: The money the provides pay.

Patient paying is often a risk. Scenarios when patient has to pay:
Low Insurance - These insurance provides put most of the burden on patients.
Private Clinics
Deductibles

2 objectives for AR
-Bring cash
-also minimize the collection period

KPIs to measure AR and set benchmarks: https://gentem.com/blog/revenue-cycle-kpis-definitions-and-benchmarks/
1. AR > 90 days
2. Days in AR
3. etc

Datasets
==========
EMR Data - Electronic Medical Records (Azure SQL DB)
    - Patients
    - HCP/Providers
    - Department
    - Transactions
    - Encounter 
Claims Data
NPI Data
ICD Data
