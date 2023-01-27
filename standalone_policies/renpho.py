from tools.ontology_helpers import make


def process_renpho(onto):

    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyWebsite = "https://renpho.com/pages/renpho-privacy-policy"
    policy_instance.considersAgent.extend([user, first_party, third_party])

    return


    #########################################################################
    # By accessing the Services on any computer, mobile phone, tablet, or other device, making a purchase from Renpho, or otherwise interacting with Renpho, YOU PROMISE US THAT (I) YOU HAVE READ, UNDERSTAND, AND AGREE TO THIS PRIVACY POLICY, AND (II) YOU ARE OVER 13 YEARS OF AGE (OR HAVE HAD YOUR PARENT OR GUARDIAN READ AND AGREE TO THIS PRIVACY POLICY FOR YOU). If you do not agree, or are unable to make this promise, you must not use the Services. In such case, you must (a) delete your account and contact us to request deletion of your data; (b) cancel any subscriptions using the functionality provided by Apple (if you are using iOS), Google (if you are using Android), any other app stores that may be available from time to time, or by us if you purchased directly from our Services; and (c) delete the App from your devices.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Renpho may modify this Privacy Policy at any time, and will post the current version on this website with the date it was last revised. If we make any material changes, we will provide you with additional notice. We encourage you to periodically review our Privacy Policy to stay informed about how we are using the data we collect. You will be deemed to have accepted the changes in any revised Privacy Policy by your continued use of the Services after the date such revised Privacy Policy is posted.  

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We may collect any data you choose to provide directly to us, for example when making a purchase, creating or using an account, using our products and their health-related features, seeking customer service or otherwise interacting with us, or being referred to us by a friend or family member. 

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # In order to use some of our apps or websites, we may ask you to enter your name, email, gender, date of birth, current weight and height, target weight, fitness level, areas for improvement, and food preferences, and ask other onboarding questions. In some of our Services, you are able to skip some of the onboarding questions by tapping on Skip or similar options.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # You can use the relevant features of Renpho’s health equipment without creating an account. However, creating an account and sharing your personal data allows Renpho to provide you with enhanced health-related insights and Services, including providing health information and recommendations that are most relevant to you and your family, providing insights and analysis of your health tendencies, providing customized health reminders, and overall providing a more personalized, fulfilling user experience.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Contact, account, and communications information: such as name, consignee information, address, email address, phone number, gender, date of birth, personal description and photograph or avatar, social media handle and profile photograph or avatar, the content of reviews or comments, complaints, inquiries, or messages to us, and any information friends or family share with us about you, such as if they refer you to Renpho. From our customers when they visit the Services, call us, sign-up for emails or another Service, or otherwise interact with us. Additionally, we may obtain your information, including any other information in this chart, in connection with a contest, sweepstakes, event, offering, or other promotional activity that is jointly offered by us and any third parties. By entering such contest or sweepstakes, you authorize and direct us to share your information with our co-sponsor(s) and any third-party service provider who administers the activity. To provide our Services, including to fulfill your requests for products, respond to your inquiries,  send you a confirmation email when you make a purchase, verify your identity, contact you with Services updates, newsletters, other informational and promotional materials from us, and third party marketing offers from our trusted partners or other companies, provide interest-based advertising to you, and meet legal obligations. Select marketing, information technology, or other third-party service providers, partners, and affiliates. The term “third-party service providers” refers to companies that provide services such as payment processing, shipping services, data analysis, email delivery, hosting services, customer service, marketing assistance, etc. The term “partners” refers to businesses that we may partner with for various endeavors, e.g., co-sponsoring promotions or sweepstakes. The term "affiliates" refers to businesses related to Renpho by common ownership or control. Renpho will require all third parties with whom we share your personal data, including third-party service providers, partners, and affiliates, to honor this Privacy Policy, and all will be contractually prohibited from using your personal data for any purpose other than in accordance with the terms of their agreements with Renpho. We will disclose your personal data to third parties only to the extent that it is related to such agreements.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Browsing information: such as IP address, MAC address, hardware ID, IDFA, and AAID; unique identifiers associated with your device including device settings (e.g., language and time zone settings); your operating system, browser type, internet service provider,  mobile carrier, and network type and signals; debugging information, pages and content that you visit on the Services, what you click on, the state and country from which you access the Services, date and time of your visit, the number of times you return to the Services, web pages you linked to our Services from, and other clickstream data. Our Services and your interactions with the Services, including through the use of cookies and other tracking technologies explained further below. To review Services usage and operations, provide interest-based advertising to you based on the way you browse and shop on the Services and other platforms, address problems with the Services, protect the security or integrity of the Services and our business, monitor the Services for compliance with our Terms of Use and the law, or meet other legal obligations. Our third-party service providers, partners, and affiliates who help us with fraud protection, website analytics, and marketing.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Payment information: name, card issuer and card type, credit or debit card number, expiration date, CVV code, and billing address. From our customers and their payment card issuers. Authorizing of credit card and other financial transactions. Our third-party service providers who process payments for us. In addition to the requirements noted above that Renpho places on third parties, third-party service providers who process payments are contractually and by law required to comply with the Payment Card Industry Data Security standards.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Biometric information: such as your exercise, activity, sleep, or health data, including the number of steps taken, distance traveled, calories burned, active minutes, weight, heart rate, blood pressure, female health data, Live Coaching Services data, and any similar information to which you grant us access from another service. See the biometric data you may provide through specific Renpho products below. From our customers when they sync their products to an account with Renpho. To provide personalized health-related Services and interest-based advertising. Our third-party service providers, partners, and affiliates who support the functionality of, and syncing with, the health-related Services.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Accident information: details about any accident, injury, or health incident regarding our products. From you, witnesses, or those who have observed you. To get you the help you need and deal with the emergency services or insurance and claims. Law enforcement and other governmental authorities in accordance with applicable law, and our professional advisors.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Suspected crime information: details of your identity, image, name and address, suspected or alleged thefts, fraud, assault or other criminal behavior. From crime and fraud prevention agencies, from you, witnesses, and from the police. To protect customers, the public, and our business against risks and crime. Law enforcement and other governmental authorities in accordance with applicable law, and our professional advisors.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # location information: location of device, location of the user accessing our website(s) or mobile app(s). From mobile device system. To enable scanning of our Bluetooth equipped products, and to obtain weather information. Our third-party service providers.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Through smart body scales: weight, BMI, body fat, fat-free body weight, subcutaneous fat, visceral fat, body water, skeletal muscle, muscle mass, bone mass, protein, BMR, and metabolic age; Through food scales: weight, calories, protein, total fat, cholesterol, sodium, total carbohydrate, dietary fiber, total sugars, and levels of vitamin D (D2+D3), vitamin A, vitamin E, vitamin C, vitamin B6, vitamin B12, calcium, iron, potassium, magnesium, manganese, zinc, copper, phosphorus, selenium, retinol equivalent, and niacin; Through smart measuring tapes: neck, shoulder, bust, waist, abdomen, hip, biceps, thigh, and calf measurements, and waist-hip ratios; Through blood pressure cuffs: SYS, DIA, and BPM; Through AI bikes: exercise duration, distance, calories, power, cadence, and resistance; and Through smart jump ropes: exercise duration, calories, average jump speed, number of jumps, number of tangles, and maximum consecutive jumps.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Location information: We collect location information to enable the properly functioning of our products, website(s) and mobile app(s). We will enable the search function of Bluetooth devices according to the authorization of location information, and provide corresponding suggestions according to your location information. If you refuse the location function in the service, you may not be able to use some of the functions of our products, website(s) or mobile apps.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # By entering your phone number in the checkout and initializing a purchase, subscribing via our subscription form or a keyword, you agree that we may send you text notifications (for your order, including abandoned cart reminders) and text marketing offers. Text marketing messages will not exceed [INSERT A NUMBER] a month. You acknowledge that consent is not a condition for any purchase.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If you wish to unsubscribe from receiving text marketing messages and notifications reply with STOP to any mobile message sent from us or use the unsubscribe link we provided you with in any of our messages. You understand and agree that alternative methods of opting out, such as using alternative words or requests will not be accounted as a reasonable means of opting out. Message and data rates may apply. For any questions please text HELP to the number you received the messages from. You can also contact us for more information. If you wish to opt out please follow the procedures above.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # With Your Consent –  We may disclose your personal data with your express consent.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We do not sell any personal data to third parties. Sometimes we send offers to selected groups of Renpho customers on behalf of other businesses. When we do this, we do not give that business your personal data.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Please note that if you voluntarily submit any personal data for posting on the Services, including social media, such as a review, comment, or “like,” the information becomes publicly available and can be collected and used by others, so you should use care before posting information about yourself online.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # In some jurisdictions, individuals may have the right to opt-in or withdraw consent for certain uses. If you reside in such jurisdictions, you may have additional rights which are detailed below, in “User Rights and Choices Regarding Personal Data,” “California Privacy Rights,” or “European Data Protection Rights.”

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # When you visit the Services, we may automatically collect certain data from you, including your device-identifying data such as IP address, MAC address, hardware ID, IDFA, and AAID; unique identifiers associated with your device including device settings (e.g., language and time zone settings); your operating system, browser type, internet service provider,  mobile carrier, and network type and signals; debugging information, pages and content that you visit on the Services, what you click on, the state and country from which you access the Services, date and time of your visit, the number of times you return to the Services, web pages you linked to our Services from, and other clickstream data.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Like many commercial websites, we analyze how visitors use our Services online through what is known as "cookie" technology or similar tracking tools. A cookie is a small text file that is placed on your computer when you access the Services online and allows us to recognize you each time you visit the Services online. We may use cookies to: (1) allow you to use the Services without having to re-enter your user name and password; (2) enhance or personalize your Services usage and shopping experience; (3) monitor Services usage; (4) manage the Services; and (5) improve the Services and our products, including providing you with interest-based ads. For more information on our advertising, see below: “Interest-Based Advertising.”

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We use the service Google Analytics to measure our web traffic and how people use our site. You can learn more about Google Analytics’ privacy policies and opt out of Google Analytics cookies at the following links: Google Privacy Policy Google Analytics Opt-out Add-on (by Google)

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If you choose, you can set your browser to reject cookies or you can manually delete individual cookies or all of the cookies on your computer by following your browser’s help file directions. You can learn more about how to change your cookie settings on common browsers by clicking on the following links: Google Chrome Firefox Safari Internet Explorer. However, if your browser is set to reject cookies or you manually delete cookies, you may have some trouble accessing and using some of the pages and features that are currently on our Services, or that we may put on our Services in the future. You may not decline web beacons. However, they can be rendered ineffective by declining all cookies or by modifying your web browser’s settings to notify you each time a cookie is tendered, permitting you to accept or decline cookies on an individual basis. Note that browser-management tools for cookies are outside of our control and we cannot guarantee their effectiveness.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # When you access the Services through a social network, we also collect data from the social network in accordance with your settings on the social network. This data may include your username, friends or followers, check-ins, and likes, and you may choose to grant or deny us access to such permissions. For more information regarding any such permissions, refer to the permissions reference pages of the social media networks with which you have an account. For more information regarding Facebook and Instagram permissions, refer to the Facebook Permissions Reference page.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We may combine the data we collect through cookies, web beacons, social medial permissions, or other technology tools with other data we have collected from you or data from other sources.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We may use aggregated, deidentified data from the above sources for statistical analysis, research, commercial, and other purposes. Aggregate, deidentified data is not “personal data,” “personal information,” or “your” data or information under this Privacy Policy or under law. We may share aggregate, deidentified data about Services users with third parties to help us understand our user demographic, including user demographic interests, habits, and usage patterns for certain of our Services so that we may market our products more effectively.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # In particular, we may share certain information with Facebook that allows us to create Custom or Lookalike Audiences. You may learn more about Facebook Lookalike Audiences here and how to opt out of having your off-Facebook activity sent to Facebook here. We encourage you to review Facebook's Privacy Policy here.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # You have the choice to tell us not to collect and use this data, and in some jurisdictions, we will only engage in interest-based advertising if you opt-in. If you would like more information about this practice and to know your choices concerning interest-based ads, visit:

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Our Services and products may include third-party products, services, and links to third-party websites, including social media, advertisements, apps, and external services that are not affiliated with us. Our Privacy Policy does not apply to products and services offered by third parties, including third-party apps such as FitBit and Apple Health that you have the option to sync with our products. When you use such products or services, the third parties may collect your data, and we cannot guarantee the safety and privacy of your data in that circumstance. For this reason, we strongly suggest that you read the third party's Privacy Policy, just as you have taken the time to read ours. We are not responsible for the content or privacy and security practices and policies of any third parties.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # The Services are not directed to children, and we do not knowingly collect data from or market to children under the age of 13 without verifiable parental consent. If you become aware of any data we have collected from children under age 13, please contact us using the contact information provided below, and we will endeavor to investigate and delete such information from our systems.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If you sign up for our mailing list, we will send you informational emails about offers of Services. At any time, you can ‘unsubscribe’ yourself from our email list simply by clicking the “unsubscribe” button.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If you do not wish to receive communications from us about special offers and promotions, you can opt-out of receiving these communications by following the instructions contained in the messages you receive. Even if you opt-out of receiving these messages, we reserve the right to send you certain communications relating to the Services we provide, and we may send you Services announcements and administrative messages. We do not offer you the opportunity to opt-out of receiving those communications. For more information about interest-based advertising, including how you can manage advertising, please see above: “Interest-Based Advertising.”

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # You may at any time review or change the data in your account or terminate your account by: Logging into your account settings and updating your account; or Contacting us using the contact information provided below in: “Contact Us.”

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Upon your request to terminate your account, we will deactivate or delete your account and personal data from our active databases. However, some data may be retained in our files for permitted or required uses, such as to prevent fraud, troubleshoot problems, assist with any investigations, enforce our Terms of Use and/or comply with legal requirements.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # You may also exercise your rights, subject to applicable laws, to request that we provide you with certain information on the personal data we have collected about you, or to correct, delete, or restrict our access to your personal data. Please note that we may retain certain data as required or permitted by applicable law. If you are a California resident or European or UK citizen, your specific rights are detailed, respectively, in the “California Privacy Rights” and “European Data Protection Rights” sections below. Under the laws of some regions and countries, we have the power to refuse your requests that are unreasonable or for which access is not required by local law.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # California laws afford consumers residing in California certain rights with respect to their personal data. If you are a California resident, this section applies to you.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Users who are California residents may request and obtain from us, once a year and free of charge, information about categories of personal information (if any) we disclosed to third parties for their own direct marketing purposes, as well as the names and addresses of all such third parties with which we shared personal information in the immediately preceding calendar year. If you are a California resident and would like to make such a request, please submit your request in writing to us using the contact information provided below in: “Contact Us.”

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If you are under 18 years of age, reside in California, and have a registered account with the Website, you have the right to request removal of unwanted data that you publicly post on the Website. To request removal of such data, please contact us using the contact information provided below, and include the email address associated with your account and a statement that you reside in California. We will make sure the data is not publicly displayed on the Website, but please be aware that the data may not be completely or comprehensively removed from our systems.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If you are a California resident, the California Consumer Privacy Act ("CCPA") provides you with the following rights that are in addition to those set forth elsewhere in this Privacy Policy regarding our use of your personal information: The right to know the categories or specific personal information we have collected, used, disclosed and sold about you. To submit a request to know, you may contact us by email at: privacy@renpho.com. You also may designate an authorized agent to make a request for access on your behalf. The right to request that we delete any personal information we have collected about you. To submit a request for deletion, you may contact us by email at: privacy@renpho.com. You also may designate an authorized agent to make a request for deletion on your behalf. Please note that we may retain certain information as required or permitted by applicable law. 

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # When you exercise these rights and submit a request to us, we will verify your identity by asking you for your email address, telephone number, order number, the last four digits of a credit or debit card used on our Website, or other uniquely identifying information. We also may use a third party verification provider to verify your identity. Your exercise of these rights will have no adverse effect on the price and quality of our goods or Services.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # European law provides citizens of countries located in the European Economic Area and the United Kingdom with the following rights with respect to their personal data:

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # The right to access – You have the right to request copies of your personal data. We may charge you a small fee for this service.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # The right to rectification – You have the right to request that Renpho correct any of your personal data you believe is inaccurate. You also have the right to request Renpho to complete your personal data that you believe is incomplete.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # The right to erasure – You have the right to request that Renpho erase your personal data. Please note that we may retain certain data as required or permitted by applicable law. 

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # The right to restrict processing – You have the right to request that Renpho restrict the processing of your personal data, subject to the conditions in this Privacy Policy.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # The right to object to processing – You have the right to object to Renpho’s processing of your personal data, subject to the conditions in this Privacy Policy.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # The right to data portability – You have the right to request that Renpho transfer your personal data that we have collected to another organization, or directly to you, subject to the conditions in this Privacy Policy and so long as such transfer will not adversely affect the rights and freedoms of others.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We maintain reasonable and appropriate measures designed to maintain data we collect in a secure manner. We have taken certain physical, electronic, and administrative steps to safeguard and secure the data we collect from visitors to the Services. Even though we follow reasonable procedures to try to protect the data in our possession, no security system is perfect and we cannot promise, and you should not expect, that your data will be secure in all circumstances.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We will never ask for your account password, and we recommend that you do not disclose your password to anyone else. We are not responsible for any of the following circumstances, including without limitation: (1) Any disclosure of personal data made under the laws, regulations, or other mandatory provisions of the government; (2) The disclosure of any personal data resulting from the fact that you have communicated the user's password to another person or shared the account with others; and (3) Any legal disputes and consequences arising from the disclosure of personal data caused by companies we do not own or control, as well as by persons we do not employ or manage.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Personal data that we collect, access, or process will be retained only as long as necessary for the fulfilment of the purposes for which it was collected, unless otherwise provided in agreements between you and Renpho or as required or authorized by law. Personal data that is no longer required to fulfill the identified purposes will be destroyed, erased, aggregated, or made deidentified.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )