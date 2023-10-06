

def parse_identifiability(o, r, fp, data):
    properties = []

    if "selectedText" not in r["attributes"]["Identifiability"].keys():
        return properties

    if r["attributes"]["Identifiability"]["value"] == "Aggregated or anonymized":
        properties.append(o.property('binded_to', o.individual(
            'Protection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('has_mechanism', o.individual('PseudoAnonymization', r["attributes"]["Identifiability"]["selectedText"])),
                *data,
            ]
        )))
    
    return properties
    

def parse_data(o, r, u):
    properties = []

    if "selectedText" not in r["attributes"]["Personal Information Type"].keys():
        return properties

    if r["attributes"]["Personal Information Type"]["value"] == "Health":
        properties.append(o.property('applies_to', o.individual(
            'HealthData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Cookies and tracking elements":
        properties.append(o.property('applies_to', o.individual(
            'TrackingData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Personal identifier":
        properties.append(o.property('applies_to', o.individual(
            'AccountData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "IP address and device IDs":
        properties.append(o.property('applies_to', o.individual(
            'DeviceData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Financial":
        properties.append(o.property('applies_to', o.individual(
            'FinancialData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "User online activities":
        properties.append(o.property('applies_to', o.individual(
            'AccountData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "User profile":
        properties.append(o.property('applies_to', o.individual(
            'SensitiveData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Contact":
        properties.append(o.property('applies_to', o.individual(
            'NonSensitiveData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Other":
        properties.append(o.property('applies_to', o.individual(
            'Data', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Computer information":
        properties.append(o.property('applies_to', o.individual(
            'DeviceData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Survey data":
        properties.append(o.property('applies_to', o.individual(
            'SensitiveData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Generic personal information":
        properties.append(o.property('applies_to', o.individual(
            'GenericData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Demographic":
        properties.append(o.property('applies_to', o.individual(
            'SensitiveData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Social media data":
        properties.append(o.property('applies_to', o.individual(
            'NonSensitiveData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Personal Information Type"]["value"] == "Location":
        properties.append(o.property('applies_to', o.individual(
            'TrackingData', 
            r["attributes"]["Personal Information Type"]["selectedText"],
            [o.property('provided_by', u)])))
            
    return properties


def parse_data_access(o, r, u):
    properties = []

    if "selectedText" not in r["attributes"]["Access Scope"].keys():
        return properties

    if r["attributes"]["Access Scope"]["value"] == "User account data":
        properties.append(o.property('applies_to', o.individual(
            'AccountData', 
            r["attributes"]["Access Scope"]["value"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Access Scope"]["value"] == "Other data about user":
        properties.append(o.property('applies_to', o.individual(
            'NonSensitiveData', 
            r["attributes"]["Access Scope"]["value"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Access Scope"]["value"] == "Profile data":
        properties.append(o.property('applies_to', o.individual(
            'SensitiveData', 
            r["attributes"]["Access Scope"]["value"],
            [o.property('provided_by', u)])))

    if r["attributes"]["Access Scope"]["value"] == "Transactional data":
        properties.append(o.property('applies_to', o.individual(
            'FinancialData', 
            r["attributes"]["Access Scope"]["value"],
            [o.property('provided_by', u)])))

    return properties


def parse_purpose(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Purpose"].keys():
        return properties

    if r["attributes"]["Purpose"]["value"] == "Additional service/feature":
        properties.append(o.property('has_purpose', o.individual('ServiceProvision', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Analytics/Research":
        properties.append(o.property('has_purpose', o.individual('Analytics', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Legal requirement":
        properties.append(o.property('has_basis', o.individual('LegalBasis', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Other":
        properties.append(o.property('has_purpose', o.individual('DataActivityPurpose', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Advertising":
        properties.append(o.property('has_purpose', o.individual('Marketing', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Merger/Acquisition":
        properties.append(o.property('has_purpose', o.individual('DataActivityPurpose', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Marketing":
        properties.append(o.property('has_purpose', o.individual('Marketing', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Personalization/Customization":
        properties.append(o.property('has_purpose', o.individual('ServiceEnhancement', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Service operation and security":
        properties.append(o.property('has_purpose', o.individual('Security', r["attributes"]["Purpose"]["selectedText"])))

    if r["attributes"]["Purpose"]["value"] == "Basic service/feature":
        properties.append(o.property('has_purpose', o.individual('ServiceProvision', r["attributes"]["Purpose"]["selectedText"])))
    
    return properties


def parse_purpose_retention(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Retention Purpose"].keys():
        return properties
    
    if r["attributes"]["Retention Purpose"]["value"] == "Analytics/Research" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        properties.append(o.property('has_purpose', o.individual('Analytics', r["attributes"]["Retention Purpose"]["selectedText"])))
    
    if r["attributes"]["Retention Purpose"]["value"] == "Perform service" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        properties.append(o.property('has_purpose', o.individual('ServiceProvision', r["attributes"]["Retention Purpose"]["selectedText"])))
    
    if r["attributes"]["Retention Purpose"]["value"] == "Other" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        properties.append(o.property('has_purpose', o.individual('DataActivityPurpose', r["attributes"]["Retention Purpose"]["selectedText"])))
    
    if r["attributes"]["Retention Purpose"]["value"] == "Legal requirement" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        properties.append(o.property('has_basis', o.individual('LegalBasis', r["attributes"]["Retention Purpose"]["selectedText"])))
    
    if r["attributes"]["Retention Purpose"]["value"] == "Advertising" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        properties.append(o.property('has_purpose', o.individual('Marketing', r["attributes"]["Retention Purpose"]["selectedText"])))
    
    if r["attributes"]["Retention Purpose"]["value"] == "Marketing" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        properties.append(o.property('has_purpose', o.individual('Marketing', r["attributes"]["Retention Purpose"]["selectedText"])))
    
    if r["attributes"]["Retention Purpose"]["value"] == "Service operation and security" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        properties.append(o.property('has_purpose', o.individual('Security', r["attributes"]["Retention Purpose"]["selectedText"])))
    
    return properties


def parse_period_retention(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Retention Period"].keys():
        return properties
    
    if r["attributes"]["Retention Period"]["value"] != "not-selected":
        properties.append(o.property('lasts_for', o.individual('DataRetentionTime', r["attributes"]["Retention Period"]["selectedText"])))
    
    return properties


def parse_mechanism_fp(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Action First-Party"].keys():
        return properties
    
    if r["attributes"]["Action First-Party"]["value"] == "Collect from user on other websites" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('ThroughWebsite', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Receive from other service/third-party (named)" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('UserSpecific', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Track user on other websites" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('ThroughWebsite', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Collect on mobile website" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('ThroughWebsite', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Receive from other service/third-party (unnamed)" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('UserSpecific', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Other" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('UserSpecific', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Collect in mobile app" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('ThroughServiceApp', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Collect on website" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('ThroughWebsite', r["attributes"]["Action First-Party"]["selectedText"])))
    
    if r["attributes"]["Action First-Party"]["value"] == "Receive from other parts of company/affiliates" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('UserSpecific', r["attributes"]["Action First-Party"]["selectedText"])))
    
    return properties


def parse_mechanism_security(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Security Measure"].keys():
        return properties

    if r["attributes"]["Security Measure"]["value"] == "Data access limitation":
        properties.append(o.property('has_mechanism', o.individual('AccessControls', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Generic":
        properties.append(o.property('has_mechanism', o.individual('TechnicalMeasure', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Secure user authentication":
        properties.append(o.property('has_mechanism', o.individual('AccessControls', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Secure data storage":
        properties.append(o.property('has_mechanism', o.individual('SecureStorage', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Other":
        properties.append(o.property('has_mechanism', o.individual('SecurityMechanism', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Privacy review/audit":
        properties.append(o.property('has_mechanism', o.individual('OrganizationalMeasure', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Privacy/Security program":
        properties.append(o.property('has_mechanism', o.individual('TechnicalMeasure', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Secure data transfer":
        properties.append(o.property('has_mechanism', o.individual('SecureTunnel', r["attributes"]["Security Measure"]["selectedText"])))

    if r["attributes"]["Security Measure"]["value"] == "Privacy training":
        properties.append(o.property('has_mechanism', o.individual('SecurityTraining', r["attributes"]["Security Measure"]["selectedText"])))

    return properties


# Extend
def parse_mechanism_tp(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Action Third Party"].keys():
        return properties
    
    if r["attributes"]["Action Third Party"]["value"] == "Collect from user on other websites" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Receive from other service/third-party (named)" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Track user on other websites" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Collect on mobile website" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Receive from other service/third-party (unnamed)" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Other" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Collect in mobile app" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Collect on website" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    if r["attributes"]["Action Third Party"]["value"] == "Receive from other parts of company/affiliates" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        properties.append(o.property('has_mechanism', o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])))
    
    return properties


def parse_mechanism_choice(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Choice Type"].keys():
        return properties
    
    if r["attributes"]["Choice Type"]["value"] != "not-selected":
        properties.append(o.property('has_mechanism', o.individual('Manual', r["attributes"]["Choice Type"]["selectedText"])))
    
    return properties


def parse_mechanism_policy_change(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Notification Type"].keys():
        return properties

    if r["attributes"]["Notification Type"]["value"] == "Personal notice":
        properties.append(o.property('has_mechanism', o.individual('FPSpecific', r["attributes"]["Notification Type"]["selectedText"])))

    if r["attributes"]["Notification Type"]["value"] == "General notice on website":
        properties.append(o.property('has_mechanism', o.individual('OnWebsitePage', r["attributes"]["Notification Type"]["selectedText"])))

    if r["attributes"]["Notification Type"]["value"] == "General notice in privacy policy":
        properties.append(o.property('has_mechanism', o.individual('InPrivacyPolicy', r["attributes"]["Notification Type"]["selectedText"])))

    if r["attributes"]["Notification Type"]["value"] == "Other":
        properties.append(o.property('has_mechanism', o.individual('FPSpecific', r["attributes"]["Notification Type"]["selectedText"])))

    return properties


def parse_mode_fp(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["Collection Mode"].keys():
        return properties
    
    if r["attributes"]["Collection Mode"]["value"] == "Unspecified":
        properties.append(o.property('has_mode', o.individual('DataTransmissionMode', r["attributes"]["Collection Mode"]["selectedText"])))
    
    if r["attributes"]["Collection Mode"]["value"] == "Implicit":
        properties.append(o.property('has_mode', o.individual('Permanent', r["attributes"]["Collection Mode"]["selectedText"])))
    
    if r["attributes"]["Collection Mode"]["value"] == "Explicit":
        properties.append(o.property('has_mode', o.individual('ByRequest', r["attributes"]["Collection Mode"]["selectedText"])))
    
    return properties


def parse_cause_policy_change(o, r):
    properties = []

    if "selectedText" not in r["attributes"]["User Choice"].keys():
        return properties

    if r["attributes"]["Change Type"]["value"] == "Privacy relevant change":
        properties.append(o.property('has_cause', o.individual('PrivacyRelated', r["attributes"]["User Choice"]["selectedText"])))

    if r["attributes"]["Change Type"]["value"] == "Non-privacy relevant change":
        properties.append(o.property('has_cause', o.individual('NonPrivacyRelated', r["attributes"]["User Choice"]["selectedText"])))

    if r["attributes"]["Change Type"]["value"] == "In case of merger or acquisition":
        properties.append(o.property('has_cause', o.individual('MergeAcquisition', r["attributes"]["User Choice"]["selectedText"])))

    if r["attributes"]["Change Type"]["value"] == "Other":
        properties.append(o.property('has_cause', o.individual('PolicyChangeCause', r["attributes"]["User Choice"]["selectedText"])))

    return properties
