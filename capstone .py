#Bungoma County Healthcare Management and Analysis
#Capstone project
print("Analyzing healthcare access and resources in Bungoma County")
import pandas as pd
import sqlite3
conn = sqlite3.connect("healthcare.db")
def run_query(sql,conn):
    result = pd.read_sql_query(sql, conn)
    print(result)
    return result
# check the exact county column name and how "Bungoma"appears
print(pd.read_sql_query("SELECT DISTINCT County FROM facilities LIMIT 50;", conn))
bungoma_only = pd.read_sql_query('SELECT * FROM facilities WHERE County = "BUNGOMA";', conn)
print(f"Bungoma rows: {bungoma_only.shape[0]}")
# Sub-County break down
sub_county_counts = run_query("""
    SELECT "Sub County", COUNT(*) as facility_count
    FROM facilities
    WHERE UPPER(County) = 'BUNGOMA'
    GROUP BY "Sub county"
    ORDER BY facility_count DESC
    """, conn)
secondary_hospitals = run_query("""
    SELECT "Sub County",COUNT(*) as count
    FROM facilities
    WHERE UPPER(County) = 'BUNGOMA' AND "facility type" ='Secondary care hospitals'
    GROUP BY "Sub County"
    ORDER BY count DESC
    """, conn)
facility_level_count = run_query("""

    SELECT "Facility level", COUNT(*) AS count
    FROM facilities
    WHERE UPPER(County) = 'BUNGOMA'
    GROUP BY "facilities level"
    ORDER BY count DESC
    """, conn)
#Overwrite the facilities table so it now holds Bungoma data
bungoma_only.to_sql("facilities", conn, if_exists="replace", index=False)

bungoma_only.to_csv("bungoma_clean.csv", index=False)
print(f"Exported {len(bungoma_only)} rows to bungoma_clean.csv")
print("faciities table now contains Bungoma-only data")
connection = sqlite3.connect("healthcare.db")
df = pd.read_excel("kenya-health-facilities-2017_08_02.xlsx")
# df.to_sql("facilities",connection,if_exists="replace",index=False)
cursor =connection.cursor()
cursor.execute("SELECT Name FROM facilities LIMIT 5")
print(cursor.fetchall())
#print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
# practice sql queries

print(df.shape)
print(df.columns)
print(df.head())
bungoma = df[df["County"] == "BUNGOMA"]
print(bungoma.shape) 
print (bungoma.columns)
for column in bungoma.columns:
    print(column)
print(bungoma["Facility type"].value_counts())
print(df["County"].unique())
print(bungoma["Owner"].value_counts())
print(bungoma["Owner"].value_counts().sum())
print(bungoma["Facility type"].isna().sum())
print(bungoma["Owner"].isna().sum())
print(bungoma["Facility type"].value_counts().sum())
print(bungoma.shape[0])
print(bungoma["Facility type"].value_counts())
print(bungoma["Facility type"].unique()) 

import matplotlib.pyplot as plt
bungoma["Owner"].value_counts().plot(kind="bar")
plt.title("Bungoma County Health Facilities by Ownership")
plt.xlabel("Owner")
plt.ylabel("Number of Facilities")
plt.tight_layout()
plt.savefig("Charts/bungoma_ownership.png")
plt.show()

bungoma["Facility type"].value_counts().plot(kind="bar")
plt.title("Bungoma County Health Facilities by Facility Type")
plt.ylabel("Number of Facilities")
plt.xlabel("Facility type")
plt.tight_layout()
plt.savefig("Charts/bungoma_facility_type.png")
plt.show()
print(bungoma.groupby("Owner")["Facility type"].value_counts())
with open("owner_facility_crosstab.txt","w")as f:
    f.write(str(bungoma.groupby("Owner")["Facility type"].value_counts()))
    print(df[["Beds",
    "Cots"]].describe())
    print("Total beds:",
    df["Cots"].sum())
bed_capacity = run_query("""
SELECT "Sub County", SUM("Beds") as total_beds, SUM("Cots") as total_cots, COUNT(*) as facility_count
FROM facilities
GROUP BY "Sub County"
ORDER BY total_beds DESC """, conn)
conn.close()