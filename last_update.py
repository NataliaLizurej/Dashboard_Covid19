import pandas as pd

# Github links
global_Confirmed = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
global_Recovered = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
global_Deaths = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
global_Vaccinations = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")

hospital = pd.read_json("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/internal/megafile--hospital-admissions.json")
vc_poland = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Poland.csv")

#Pandas
#Global Cases:
gc = global_Confirmed[global_Confirmed.columns[-1]].sum()
#Global Recovered:
gr = global_Recovered[global_Recovered.columns[-1]].sum()
#Global Deaths:
gd = global_Deaths[global_Deaths.columns[-1]].sum()
#Vaccinations:
u = global_Vaccinations.index[-1] #ostatni indeks
z = global_Vaccinations['date'].loc[u] #ostatnia data
#Total Vaccinations
gv = global_Vaccinations[global_Vaccinations.columns[3]][(global_Vaccinations['location'] == 'World') & (global_Vaccinations['date'] == z)].sum()
#People vaccinated
gv_people = global_Vaccinations[global_Vaccinations.columns[4]][(global_Vaccinations['location'] == 'World') & (global_Vaccinations['date'] == z)].sum()
#People fully vaccinated
gv_people_full = global_Vaccinations[global_Vaccinations.columns[5]][(global_Vaccinations['location'] == 'World') & (global_Vaccinations['date'] == z)].sum()
#Number of Country/Regions:
g_country_regions = global_Confirmed['Country/Region'].nunique() # jest 192

date_poland_vaccines = vc_poland['date'].iloc[-1]

h = hospital[hospital['location'] == 'Poland'].date.max() #zmienna pomocnicza - do uzyskania najbardziej aktualnej daty dla POLSKI
hospital_poland = hospital['hosp_patients'][(hospital['location'] == 'Poland') & (hospital['date'] == h)] #ilosc osob hospitalizowanych w POLSCE

total_vaccines_poland = vc_poland['total_vaccinations'].iloc[-1] #zuzyte szczepionki w Polsce
people_vaccines_poland = vc_poland['people_vaccinated'].iloc[-1] #liczba osob zaszczepionych w Polsce
people_fully_poland = vc_poland['people_fully_vaccinated'].iloc[-1] #liczba osob zaszczepionych pelna dawka w Polsce

#Dane dot.testow dla POLSKI:
tests = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/testing/covid-testing-all-observations.csv")
global_Confirmed = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
global_Deaths = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
global_Recovered = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
#Najswiezsza liczba (zrobionych testow w Polsce)
count_test = tests[tests['Entity'] == 'Poland - people tested'].iloc[-1]['Daily change in cumulative total']

#Ostatnia data ktora zostala zaktualizowana (mam nadzieje ze pojawi sie po prostu 16 maja 2021, jak cos bedzie nie tak to poprawie) do napisu LAST UPDATE
tests_Date = tests[tests['Entity'] == 'Poland - people tested'].iloc[-1]['Date']

#Dane dot. zakazen/smierci/wyzdrowien dla POLSKI:
#data ostatnia,ktora jest pomocnicza i jednoczesnie do napisu LAST UPDATE
last_day = global_Confirmed.columns[-1]
#data przedostatnia
two_last_days = global_Confirmed.columns[-2]
#Liczba zakazen najswiezsza
daily_poland_confirmed = (global_Confirmed[global_Confirmed['Country/Region'] == 'Poland'].iloc[-1][last_day] - global_Confirmed[global_Confirmed['Country/Region'] == 'Poland'].iloc[-1][two_last_days])
#Liczba umarlych najswiezsza
daily_poland_deaths = (global_Deaths[global_Deaths['Country/Region'] == 'Poland'].iloc[-1][last_day] - global_Deaths[global_Deaths['Country/Region'] == 'Poland'].iloc[-1][two_last_days])
#Liczba wyzdrowialych najswiezsza
daily_poland_recovered = (global_Recovered[global_Recovered['Country/Region'] == 'Poland'].iloc[-1][last_day] - global_Recovered[global_Recovered['Country/Region'] == 'Poland'].iloc[-1][two_last_days])

