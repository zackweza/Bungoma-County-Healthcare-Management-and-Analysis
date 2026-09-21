# Mapping Healthcare Access Gaps in Bungoma County
## Executive summary
This analysis examines the distribution,ownership,and type of health facilities across Bungoma County using kenya's 2017 national health facilities dataset.data was cleaned and filtered to isolate Bungoma County records using python(pandas).Key aggregation-facility counts by owner type among others- were queried using SQL(SQLite) to validated pandas results and to demonstrate database-querying skill and visualized to uncover patterns in healthcare infrastructure across the county's ten sub-counties by Power BI and matplotlib.

Bungomas County has 202 registered health facilities.The Ministry of Health owns the majority - 113 facilities roughly 56% of the to facilities while the remainder is split among private practices,faith based organizations,and other providers.Most facilities are lower tier dispensaries and clinics; only 7 facilities countywide offer secondary care.Facility distribution is also geographically uneven: Kanduyi sub-county alone accounts for 44 facilities, while Sirisia has just 13.Most strikingly,half of Bungoma's ten sub-counties, -Tongaren,Kabuchai,Cheptais,Bumula, and Sirisia-have no secondary hospital.

these findings point to a healthcare system heavily reliant on government-run, lower-tier facilities,with meaningful gap in access to higher-level care concentrated in specific sub-counties.The analysis concludes with recommendation to prioritize secondary care investment and referral system improvements in the most underserved areas.

     

## Facility Ownership

### Question
Who owns the health facilities in Bungoma County?

### Finding                                                                                          Minstry of Health owns 113 of the 202 facilities

### Insight
The facility network is dominated by Ministry of Health-owned while the remaining are distributed among other providers for example,private enterprises,faith based among many others.
### Possible Action
Health Planning should consider coordination between Ministry of health facility and other providers when addresing service coverage.

## Bungoma County -initial Findings
1. Total health facilities:
    202 facilities

2. Data Structures:
    22 columns

3. Facility ownership:
    .Ministry of Health                         113 
    .Private Practice/Midwifery                  19 
    .Other Faith Based                           14 
    .Private Enterprises                        12
    .Private Practice -Clinical officer          10
    .public institutions                          8 
     Private Practice -General Practitioner       7       
    .Christian Health Association of kenya        6
    .Non Governmental Organisation                3
    .Company Medical Services                     2
    .Community                                    1
    .Laboratory Technician/Technologist           1    

4. Data quality: 
    We checked the facility type and Owner columns for missing values
## Facility type
### Question
## What types of health facilities are most common in Bungoma County?
### Finding
Dispensaries and clinics make up 149 of 202 facilities which is approximately 74%,while only 7 are secondary care hospitals in the entire county.
### Insight
Bungoma's health system relies heavily on lower-tier primary care.Relatively very few facilities exist to handle more serious or specialized cases.
### Possible Actions
Strengthen refferal systems between dispensaries and the limited secondary hospitals, and consider upgrading select high-traffic dispensaries would ease pressure on the few larger facilities.

### Question
Does facility type differ by who owns the facility

### Finding
Ministry of Health owns facilities across every tier - from 86 dispensaries down to 5 secondary care hospitals - accounting for most of bungoma's higher-tier care capacity.Other owners(Company medical services,Other faith Based) each contribute just one secondary care hospital,while most non-government owners almost exclusively at the dispensary/basic care level.

### Insight
Secondary care capacityin bungoma is heavily concentrated within the Ministry of Health(5 of roughly 7 total secondary Hospitals),with only marginal contributions from private and faith based providers.This means if government hospital capacity is strained, there is very little private/NGO secondary care to absorb overflow.
### Possible Action
Since secondary care is concentrated in government hands, health planning should focus on strengthening and expanding Ministry of Health hospital capacityspecifically, while exploring incentives for faith-based/private partners to expand beyond basic-tier care.

## Goegraphic Distribution of Facilities
###Question
Are health facilities evenly distributed across bungoma's sub- counties?
### Findings
        Facility counts vary significantly by sub-county -from 44 in kanduyi down to just 13 in sirisia.The top 3 sub-counties(kanduyi,tongaren,kabuchai)together holds 89 facilities, while the bottom 3 (Bumula,sirisia and kimili) holds roughly  a third of that.
### Insight
        kanduyi appears to be the healthcare hub of the county, likely becouse it hosts the county's main urbarn centre.Sub counties like sirisia and bumula have significantly fewer facilities, which could mean residents there travel further for care-especially for services concentrated in fewer, larger facilities(like the secondary care hospitals we found earlier)
### Possible Action
        Prioritize new facility investment - especially any planned secondary care hospitals - in the most underserved sub - counties (Bumula,sirisia and kimilili) rather than concentrating further growth in kanduyi which has already has proportionally stron coverage.
## Distribution of Health Facilities 
### Findings
        Bungoma has 202 facilities in total of which Kanduyi commands highest overally with 44 facilities while Sirisia has got the lowest with only 13 facilities.
        Secondary care hospitals are present in:
            Kimilili -      2
            Kanduyi -       2
            Webuye west-    1
            Webuye east  -  1
            Mt Elgon   -    1
This indicates that half of Bungoma sub-counties have no secondary-level care.
### Insight
Health facilities are unevenly distributed across Bungoma county,and secondary care hospitals are concentrated in only five sub-counties.This suggests that access to higher -level healthcare services may varry considerably between sub-countie, particularly for areas without secondary care hospital.
### Possible Action
The Bungoma County health management team should assess sub-counties without secondary care hospitals and consider strengthening refferal systems, upgrading selected facilities,or expanding secondary-level services where population needs to justify it.

        Sub county  total_beds  total_cots  facility_count
0      kanduyi         566          27              44
1  webuye west         353          30              18
2     kimilili         144           0              15
3     kabuchai         110           0              21
4       bumula         107           4              14
5     tongaren         102           8              24
6  webuye east          91           2              20
7     mt elgon          76           0              16
8      sirisia          56           0              13
9     Cheptais          56          21              17
### Question
Does bed capacity align with facilities count across sub-counties?
### Finding
Bed capacity does not scale proportionally with facilty count.Webuye west has only 18 facilities but 553 beds-the highest in the county-while tongaren has 24 facilities but only 102 beds.Sirisia has both the fewest facilities(13) among lowest beds capacity (56)
### Insight
Facility count alone is misleading measure of healthcare capacity.Some subcounties (like Webuye west) have fewer larger facilities with substantial capacity,while others like(like Tongaren) have nuerous but smaller facilities.Sirisia stands out as doubly disadvantaged - low on both facility count and bed capacity.
### Possible Action
Prioritize Sirisia specifically for capacity expansion, since it lacks both suffficient facility count and bed capacity - unlike other sub-counties without secondary hospitals (eg Kabuchai), which at least have moderate bed capacity to fall back on.