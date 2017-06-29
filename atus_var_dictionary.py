act_dict = {
    'TUCASEID'  : 'household case ID',
    'TUACTIVITY_N' : 'activity no, an index of separate activities, each coded',
    'TEWHERE'    : 'where activity happened',
    'TUACTDUR'   : 'duration of activity in mins',
    'TUACTDUR24' : 'duration of activity in mins',
    'TUTIER1COD' : 'first tier of activity code',
    'TUTIER2CODE': 'second tier of activity code',
    'TUTIER3CODE': 'second tier of activity code',
    'TUSTARTTIM' : 'Activity start time',
    'TUSTOPTIME' : 'Activity stop time',
    'TRCODEP'    : 'contains the six-digit activity code',
    'TRTIER1P'   : 'two-digit activity code',
    'TRTIER2P'   : 'four-digit activity code',
    'TRTEC_LN'   : 'Time spent providing eldercare during activity',
    'TRWBELIG'   : 'Flag identifying activities eligible for the Well-being Module',
    'TUCC5'      : 'Was at least one of your own household children < 13 in your care during this activity?',
    'TUCUMDUR'   : 'Cumulative duration of activity lengths in minutes. ie is all time accounted for',

}

resp_dict = {
    'TUCASEID'  :   'household case ID',
    'TULINENO'  :   'household individual, 1 = respondent',
    'TEERN'     :   'total weekly overtime earnings',
    'TEERNH1O'  :   'hourly rate of pay on your main job',
    'TEERNH2'   :   'hourly rate of pay on your main job',
    'TELFS'     :   'labor force status',
    'TRTALONE'  :   'total non-work-related time spent alone',
    'TRTALONE_WK':  'Total work- and nonwork-related time respondent spent alone ',
    'TESCHENR'  :   "enrolled in high school, college, or university",
    'TESCHLVL'  :   "would that be high school, college, or university",
    'TESPEMPNOT':   "employment status of spouse or unmarried partner",
    'TRDPFTPT'  :   "Full time or part time employment status of respondent",
    'TRERNWA'   :   "Weekly earnings at main job (2 implied decimals)",
    'TRSPFTPT'  :   "Full time or part time employment status of spouse or unmarried partner",
    'TRYHHCHILD':   "Age of youngest household child < 18",
    'TRHHCHILD' :   "Presence of household children < 18",
    'TRCHILDNUM':   "number of household children < 18",
    'TUDIARYDAY':   "day of week about which respondent interviewed (M->F = 2->6)",
    'TUDIARYDATE':  "Date of diary day",
    'TUYEAR'    :   "Year of diary day",
    'TEMJOT'    :   "Multiple job status",
    'TRTEC'     :   "Total time spent providing elder-care during diary day",
    'TRTHH'     :   "Total time spent providing secondary childcare for household children during diary day",
    'TRSPPRES'  :   "Presence of spouse",
    'TU06FWGT'  :   "2003, 2004, and 2005 data use this weight",
    'TUFINLWGT' :   "2006 and after use this weight",
    'TUFNWGTP'  :   "ATUS final weight",
    'TRWBMODR'  :   "Well being module respondent",
    'TRDTOCC1 ' :   "Detailed occupation recode (main job)",
    'TRMJIND1'  :   "Major industry recode",  #6 = Transportation and utilities
    'TRMJOCGR'  :   "Major occupation category", # 6 Production, transportation, and material moving occupations
    'TRHOLIDAY' :   "Flag to indicate if diary day was a holiday",
    'TRNUMHOU'  :   "Number of people in respondents household",
    'TRTFRIEND' :   "Total nonwork-related time respondent spent with friends",
    'TRTHHFAMILY':  "Total nonwork-related time respondent spent with household family members",
    'TRTSPONLY' :   "Total nonwork-related time respondent spent with spouse only", 
    'TRTSPOUSE' :   "Total nonwork-related time respondent spent with spouse (others may be present",
    'TRTUNMPART':   "Total nonwork-related time respondent spent with unmarried partner (others may be present)",
}


rost_dict = {
    'TUCASEID'  : 'household case ID',
    'TULINENO'  : 'household individual, 1 = respondent',
    'TEAGE'     : "respondent's age",
    'TESEX'     : "sex",
    'TERRP'     : "How is this person related to you?"
}


who_dict = {
    'TUCASEID'  : 'household case ID',
    'TULINENO'  : 'household individual, 1 = respondent',
    'TUWHO_CODE': 'Who was present during activity?',
}


cps_dict = {
    'TUCASEID'  :   'household case ID',
    'PEEDUCA'   :   "Educational Attainment",
    'GESTFIPS'  :   "State",
    'GEMETSTA'  :   "Metropolitan status... switches to GTMETSTA in 2004"
}

sum_dict = {
    'TUCASEID'  :   "household case ID",
    'TEAGE'     :   "respondents age",
    'TESEX'     :   "sex",
    'PTDTRACE'  :   "self-reported race",
    'PEHSPNON'  :   "Hispanic origin",
    'TRCHILDNUM':   "number of household children < 18",
    'TELFS'     :   "labor force status",
    'TRERNWA'   :   "Weekly earnings at main job (2 implied decimals)",
    'TEMJOT'    :   "Multiple job status",
    'TRTEC'     :   "Total time spent providing eldercare during diary day",
    'TRTHH'     :   "Total time spent providing secondary childcare for household children during diary day",
    'PEEDUCA'   :   "Educational Attainment",
    'TEHRUSLT'  :   "total hours usually worked per week (sum of TEHRUSL1 and TEHRUSL2)",
    'TESCHENR'  :   "enrolled in high school, college, or university",
    'TESCHLVL'  :   "would that be high school, college, or university",
    'TESPEMPNOT':   "employment status of spouse or unmarried partner",
    'TRDPFTPT'  :   "Full time or part time employment status of respondent",
    'TRSPFTPT'  :   "Full time or part time employment status of spouse or unmarried partner",
    'TRYHHCHILD':   "Age of youngest household child < 18",
    'TUDIARYDAY':   "day of week about which respondent interviewed (M->F = 2->6)",
    'TUYEAR'    :   "Year of diary day",
    'TRSPPRES'  :   "Presence of spouse",
    'TU06FWGT'  :   "2003, 2004, and 2005 data use this weight",
    'TUFINLWGT' :   "2006 and after use this weight",
    'TUFNWGTP'  :   "ATUS final weight",
    'GEMETSTA'  :   "Metropolitan status... switches to GTMETSTA in 2004",
    'TRHOLIDAY' :   "Flag to indicate if diary day was a holiday"
}

rost_dict = {
    'TUCASEID'  : 'household case ID',
    'TULINENO'  : 'household individual, 1 = respondent',
    'TEAGE'     : "respondent's age",
    'TESEX'     : "sex",
    'TERRP'     : "How is this person related to you?"
}


who_dict = {
    'TUCASEID'  : 'household case ID',
    'TULINENO'  : 'household individual, 1 = respondent',
    'TUWHO_CODE': 'Who was present during activity?',
}

cps_dict = {
    'TUCASEID'  :   'household case ID',
    'PEEDUCA'   :   "Educational Attainment",
    'GESTFIPS'  :   "State",
    'GEMETSTA'  :   "Metropolitan status... switches to GTMETSTA in 2004"
}



sum_dict = {
    'TUCASEID'  :   "household case ID",
    'TEAGE'     :   "respondents age",
    'TESEX'     :   "sex",
    'PTDTRACE'  :   "self-reported race",
    'PEHSPNON'  :   "Hispanic origin",
    'TRCHILDNUM':   "number of household children < 18",
    'TELFS'     :   "labor force status",
    'TRERNWA'   :   "Weekly earnings at main job (2 implied decimals)",
    'TEMJOT'    :   "Multiple job status",
    'TRTEC'     :   "Total time spent providing eldercare during diary day",
    'TRTHH'     :   "Total time spent providing secondary childcare for household children during diary day",
    'PEEDUCA'   :   "Educational Attainment",
    'TEHRUSLT'  :   "total hours usually worked per week (sum of TEHRUSL1 and TEHRUSL2)",
    'TESCHENR'  :   "enrolled in high school, college, or university",
    'TESCHLVL'  :   "would that be high school, college, or university",
    'TESPEMPNOT':   "employment status of spouse or unmarried partner",
    'TRDPFTPT'  :   "Full time or part time employment status of respondent",
    'TRSPFTPT'  :   "Full time or part time employment status of spouse or unmarried partner",
    'TRYHHCHILD':   "Age of youngest household child < 18",
    'TUDIARYDAY':   "day of week about which respondent interviewed (M->F = 2->6)",
    'TUYEAR'    :   "Year of diary day",
    'TRSPPRES'  :   "Presence of spouse",
    'TU06FWGT'  :   "2003, 2004, and 2005 data use this weight",
    'TUFINLWGT' :   "2006 and after use this weight",
    'TUFNWGTP'  :   "ATUS final weight",
    'GEMETSTA'  :   "Metropolitan status... switches to GTMETSTA in 2004",
    'TRHOLIDAY' :   "Flag to indicate if diary day was a holiday",
}

"""
File    Linking Variables
Respondent file                         TUCASEID    TULINENO (always equal to 1 on the Respondent file)
Roster file                             TUCASEID    TULINENO
Activity file                           TUCASEID    TUACTIVITY_N
Who file                                TUCASEID    TUACTIVITY_N    TULINENO
ATUS-CPS file                           TUCASEID    TULINENO
Activity summary file                   TUCASEID    
Eldercare roster file (2011 and later)  TUCASEID    TULINENO
"""


atus_meanings = {}
atus_meanings['sum'] = sum_dict
atus_meanings['act'] = act_dict
atus_meanings['cps'] = cps_dict
atus_meanings['resp'] = resp_dict
atus_meanings['rost'] = rost_dict


def get_col_meaning(col_head=None):
    out_cvses = []
    meaning = None
    for cvs_key, dict in atus_meanings.items():
        if col_head.upper() in list(dict.keys()):
            meaning = dict[col_head.upper()]
            out_cvses.append("atus_{0}.cvs".format(cvs_key))
    if not meaning:
        return None, None
    else:
        return meaning, out_cvses


# test_meaning, cvses = get_col_meaning(col_head='TULINENO')
# print(test_meaning, cvses)
