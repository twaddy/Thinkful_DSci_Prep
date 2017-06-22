# col heads of activity cvs for which I've yet to find description.
"""
TUCC5   TUCC5B  TRTCCTOT_LN TRTCC_LN    TRTCOC_LN
TUCC8   TUCUMDUR    TUCUMDUR24
TUACTDUR    TR_03CC57   TRTO_LN TRTONHH_LN  TRTOHH_LN   TRTHH_LN    TRTNOHH_LN 
TUCC7   TRWBELIG    TUEC24  TUDURSTOP
"""

def get_act_dict():
    act_dict = {
        'TUCASEID'  : 'household case ID',
        'TUACTIVITY_N' : 'activity no, an index of separate activities, each coded',
        'TEWHERE'    : 'where activity happened'
        'TUACTDUR24' : 'duration of activity in mins',
        'TUTIER1COD' : 'first tier of activity code',
        'TUTIER2CODE': 'second tier of activity code',
        'TUTIER3CODE': 'second tier of activity code',
        'TUSTARTTIM' : 'Activity start time'
        'TUSTOPTIME' : 'Activity stop time'
        'TRCODEP'       : 'contains the six-digit activity code'
        'TRTIER1P'   : 'two-digit activity code'
        'TRTIER2P'   : 'four-digit activity code'
        'TRTEC_LN'   : 'Time spent providing eldercare during activity'
    }
    return act_dict

def get_resp_dict():
    resp_dict = {
        'TUCASEID' : 'household case ID',
        'TULINENO' : 'household individual, 1 = respondent',
        'TEERN'    : 'total weekly overtime earnings',
        'TEERNH1O' : 'hourly rate of pay on your main job',
        'TEERNH2'  : 'hourly rate of pay on your main job',
        'TELFS'    : 'labor force status',
        'TRTALONE' : 'total non-work-related time spent alone',
        'TESCHENR'  :   "enrolled in high school, college, or university",
        'TESCHLVL'  :   "would that be high school, college, or university",
        'TESPEMPNOT':   "employment status of spouse or unmarried partner",
        'TRDPFTPT'  :   "Full time or part time employment status of respondent",
        'TRERNWA'   :   "Weekly earnings at main job (2 implied decimals)",
        'TRSPFTPT'  :   "Full time or part time employment status of spouse or unmarried partner",
        'TRYHHCHILD':   "Age of youngest household child < 18",
        'TRCHILDNUM':   "number of household children < 18",
        'TUDIARYDAY':   "day of week about which respondent interviewed (M->F = 2->6)",
        'TUFNWGTP'  :   "ATUS final weight",
        'TUYEAR'    :   "Year of diary day",
        'TEMJOT'    :   "Multile job status",
        'TRTEC'     :   "Total time spent providing eldercare during diary day",
        'TRTHH'     :   "Total time spent providing secondary childcare for household children during diary day",
        'TRSPPRES'  :   "Presence of spouse",
        'TUDIARYDAY':   "Day of the week",
        'TRHOLIDAY' :   "Holiday?",
        'TU06FWGT'  :   "2003, 2004, and 2005 data use this weight",
        'TUFINLWGT' :   "2006 and after use this weight",
        'TUFNWGTP'  :   "ATUS final weight",
    }
    return resp_dict


#who and roster can be linked via the TULINENO col

def get_rost_dict():
    rost_dict = {
        'TEAGE'     : "respondent's age",
        'TESEX'     :  "sex"
    }
    return rost_dict


def get_cps_dict():
    cps_dict = {
        'TUCASEID'  :   'household case ID',
        'PEEDUCA'   :   "Educational Attainment",
        'GESTFIPS'  :   "State",
        'GEMETSTA'  :   "Metropolitan status... switches to GTMETSTA in 2004"
    }
    return cps_dict



def get_sum_dict():
    sum_dict = {
        'TUCASEID'  :   'household case ID',
        'TEAGE'     :   "respondent's age",
        'TESEX'     :   "sex",
        'PTDTRACE'  :   "self-reported race",
        'PEHSPNON'  :   "Hispanic origin",
        'TRCHILDNUM':   "number of household children < 18",
        'TELFS'     :   "labor force status",
        'TRERNWA'   :   "Weekly earnings at main job (2 implied decimals)",
        'TEMJOT'    :   "Multile job status",
        'TRDPFTPT'  :   "Full or Part-time Status",
        'TRTEC'     :   "Total time spent providing eldercare during diary day",
        'TRTHH'     :   "Total time spent providing secondary childcare for household children during diary day"
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
        'TUDIARYDAY':   "Day of the week",
        'TRHOLIDAY' :   "Holiday?",
        'TU06FWGT'  :   "2003, 2004, and 2005 data use this weight",
        'TUFINLWGT' :   "2006 and after use this weight",
        'TUFNWGTP'  :   "ATUS final weight",
        'GEMETSTA'  :   "Metropolitan status... switches to GTMETSTA in 2004"
    }
    return sum_dict

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
