def information_extractor(pdf_output,tesseract_output,filename):

    input_string = pdf_output
    text = tesseract_output
    file = filename
    info = {}

    #################################### Checklist ###########################################################

    date = re.findall("\d{1,2}/\d{1,2}/\d{4}\n",input_string)
    if(date == []):
        date = re.findall("\d{1,2}/\d{1,2}/\d{4}\n",text)
        if(date!=[]):
            Date = "".join(date[0]) 
    else:
        Date = "".join(date[0])

    name = re.findall("NAME:.*\n", input_string)
    if(name == []):
        name = re.findall("NAME:.*\n", text)
        Name = "".join(name)
        Name = Name.lstrip("NAME:")
        Name = Name.lstrip(" ")
        Name = Name.rstrip(" ")
        Name = Name.replace("\n","")
        Name = Name.replace("\t","")
    else:
        Name = "".join(name[0])
        Name = Name.lstrip("NAME:")
        Name = Name.lstrip(" ")
        Name = Name.rstrip(" ")
        Name = Name.replace("\n","")
        Name = Name.replace("\t","")

    email = re.findall("\s[A-Za-z0-9'.''_']+@.*\n", input_string)
    if(email == []):
        email = re.findall("\s[A-Za-z0-9'.''_']+@.*\n",text)
        Email = "".join(email)
        Email = Email.rstrip("\n")
        Email = Email.replace("\n","")
        Email = Email.replace("\t","")
    else:
        Email = "".join(email[0])
        Email = Email.rstrip("\n")
        Email = Email.replace("\n","")
        Email = Email.replace("\t","")
    

    #Insured TSV
    #INSURED
    ins_add_line1 = re.findall("\n.*INSURER C",input_string)
    #print(ins_add_line1)
    ins_Add_1 = "".join(ins_add_line1)
    ins_Add_1 = ins_Add_1.replace("INSURER C","")
    ins_Add_1 = ins_Add_1.replace("\n","")
    ins_Add_1 = ins_Add_1.replace("\t","")
    ins_Add_1 = ins_Add_1.replace("\"","")
    #print(ins_Add_1)

    ins_add_line2 = re.findall("\n.*INSURER D",input_string)
    #print(add_line2)
    ins_Add_2 = "".join(ins_add_line2)
    ins_Add_2 = ins_Add_2.replace("INSURER D","")
    ins_Add_2 = ins_Add_2.replace("\n","")
    ins_Add_2 = ins_Add_2.replace("\t","")
    #print(Add_2)

    ins_add_line3 = re.findall("\n.*INSURER E",input_string)
    #print(add_line3)
    ins_Add_3 = "".join(ins_add_line3)
    ins_Add_3 = ins_Add_3.replace("INSURER E","")
    ins_Add_3 = ins_Add_3.replace("\n","")
    ins_Add_3 = ins_Add_3.replace("\t","")
    #print(Add_3)

    ins_Insured_Address = ins_Add_1 + " " + ins_Add_2 + " " + ins_Add_3
    #print(ins_Insured_Address)

    #INSURED
    ins_add_line1 = re.findall("\n.*INSURER C",input_string)
    ins_Add_1 = "".join(ins_add_line1)
    ins_Add_1 = ins_Add_1.replace("INSURER C","")
    ins_Add_1 = ins_Add_1.replace("\n","")
    ins_Add_1 = ins_Add_1.replace("\t","")
    ins_Add_1 = ins_Add_1.replace("\"","")
    
    ins_add_line2 = re.findall("\n.*INSURER D",input_string)
    ins_Add_2 = "".join(ins_add_line2)
    ins_Add_2 = ins_Add_2.replace("INSURER D","")
    ins_Add_2 = ins_Add_2.replace("\n","")
    ins_Add_2 = ins_Add_2.replace("\t","")
    
    ins_add_line3 = re.findall("\n.*INSURER E",input_string)
    ins_Add_3 = "".join(ins_add_line3)
    ins_Add_3 = ins_Add_3.replace("INSURER E","")
    ins_Add_3 = ins_Add_3.replace("\n","")
    ins_Add_3 = ins_Add_3.replace("\t","")
    
    ins_Insured_Address = ins_Add_1 + " " + ins_Add_2 + " " + ins_Add_3
    
    if(ins_Add_1 == ""):
        ins_add_line1 = re.findall("\n.*INSURER B",text)
        ins_Add_1 = "".join(ins_add_line1)
        ins_Add_1 = ins_Add_1.replace("INSURER B","")
        ins_Add_1 = ins_Add_1.replace("INSURED","")
        ins_Add_1 = ins_Add_1.replace("\n","")
        ins_Add_1 = ins_Add_1.replace("\t","")
        
        ins_add_line2 = re.findall("\n.*INSURER [c,C]",text)
        ins_Add_2 = "".join(ins_add_line2)
        ins_Add_2 = ins_Add_2.replace("INSURER C","")
        ins_Add_2 = ins_Add_2.replace("INSURER c","")
        ins_Add_2 = ins_Add_2.replace("\n","")
        ins_Add_2 = ins_Add_2.replace("\t","")
        
        ins_add_line3 = re.findall("\n.*INSURER D",text)
        ins_Add_3 = "".join(ins_add_line3)
        ins_Add_3 = ins_Add_3.replace("INSURER D","")
        ins_Add_3 = ins_Add_3.replace("\n","")
        ins_Add_3 = ins_Add_3.replace("\t","")
        
        ins_add_line4 = re.findall("\n?.*\n.*INSURER E",text)
        ins_Add_4 = "".join(ins_add_line4)
        ins_Add_4 = ins_Add_4.replace("INSURER E","")
        ins_Add_4 = ins_Add_4.replace("\n","")
        ins_Add_4 = ins_Add_4.replace("\t","")
        
        ins_Insured_Address = ins_Add_1 + " " + ins_Add_2 + " " + ins_Add_3 + " " + ins_Add_4
        ins_Insured_Address = ins_Insured_Address.lstrip(" ")
        
    Ins_Insured_Address = re.findall(".*\d\s*",ins_Insured_Address)
    ins_Insured_Address=""
    ins_Insured_Address = "".join(Ins_Insured_Address)
    #print("Insured : ",ins_Insured_Address)

    #PRODUCER
    prod_add_line1 = re.findall("\n.*PHONE",input_string)
    prod_Add_1 = "".join(prod_add_line1)
    prod_Add_1 = prod_Add_1.rstrip("PHONE")
    prod_Add_1 = prod_Add_1.replace("\n","")
    prod_Add_1 = prod_Add_1.replace("\t","")
    prod_Add_1 = prod_Add_1.replace("\"","")
    prod_Add_1 = prod_Add_1.lstrip(" ")
    
    prod_add_line2 = re.findall("\n.*\(A/C, No, Ext\)",input_string)
    prod_Add_2 = "".join(prod_add_line2)
    prod_Add_2 = prod_Add_2.rstrip("(A/C, No, Ext)")
    prod_Add_2 = prod_Add_2.replace("\n","")
    prod_Add_2 = prod_Add_2.replace("\t","")
    
    prod_add_line3 = re.findall("\n.*E-MAILADDRESS",input_string)
    prod_Add_3 = "".join(prod_add_line3)
    prod_Add_3 = prod_Add_3.rstrip("E-MAILADDRESS")
    prod_Add_3 = prod_Add_3.replace("\n","")
    prod_Add_3 = prod_Add_3.replace("\t","")
    
    if(prod_Add_1 == ""):
        prod_Insured_Address = prod_Add_1 + " " + prod_Add_2 + " " + prod_Add_3
        
        prod_add_line1 = re.findall(".*PHONE",text)
        prod_Add_1 = "".join(prod_add_line1)
        prod_Add_1 = prod_Add_1.replace("PHONE","")
        prod_Add_1 = prod_Add_1.replace("\n","")
        prod_Add_1 = prod_Add_1.replace("\t","")
        prod_Add_1 = prod_Add_1.replace("\"","")
        prod_Add_1 = prod_Add_1.lstrip(" ")

        prod_add_line2 = re.findall(".*\(A",text)
        prod_Add_2 = "".join(prod_add_line2)
        prod_Add_2 = prod_Add_2.replace("(A","")
        prod_Add_2 = prod_Add_2.replace("\n","")
        prod_Add_2 = prod_Add_2.replace("\t","")
    

        prod_add_line3 = re.findall(".*E-MAIL",text)
        prod_Add_3 = "".join(prod_add_line3)
        prod_Add_3 = prod_Add_3.replace("E-MAIL","")
        prod_Add_3 = prod_Add_3.replace("\n","")
        prod_Add_3 = prod_Add_3.replace("\t","")
    
    
    prod_Insured_Address = prod_Add_1 + " " + prod_Add_2 + " " + prod_Add_3
    Prod_Insured_Address = re.findall(".*\d\s*",prod_Insured_Address)
    prod_Insured_Address = ""
    prod_Insured_Address = "".join(Prod_Insured_Address)
    #print(prod_Insured_Address)
    
    INSURERA = re.findall("INSURER A :.*\n", input_string) # Number in the end is the NAIC number
    if(INSURERA == []):
        INSURERA = re.findall("INSURER\s*A:.*\n", text)    
    InsurerA = "".join(INSURERA)
    InsurerA = InsurerA.lstrip("INSURER A:")
    InsurerA = InsurerA.rstrip(" ")
    InsurerA = InsurerA.replace("\n","")
    InsurerA = InsurerA.replace("\t","")
    #print("Insurer A : ",InsurerA)

    INSURERB = re.findall("INSURER B :.*\n", input_string) # Number in the end is the NAIC number
    if(INSURERB == []):
        INSURERB = re.findall("INSURER\s*B:.*\n", text)    
    InsurerB = "".join(INSURERB)
    InsurerB = InsurerB.lstrip("INSURER B:")
    InsurerB = InsurerB.rstrip(" ")
    InsurerB = InsurerB.replace("\n","")
    InsurerB = InsurerB.replace("\t","")
    #print("Insurer B : ",InsurerB)
    
    INSURERC = re.findall("INSURER C :.*\n", input_string) # Number in the end is the NAIC number
    if(INSURERC == []):
        INSURERC = re.findall("INSURER\s*C:.*\n", text)    
    InsurerC = "".join(INSURERC)
    InsurerC = InsurerC.lstrip("INSURER C:")
    InsurerC = InsurerC.rstrip(" ")
    InsurerC = InsurerC.replace("\n","")
    InsurerC = InsurerC.replace("\t","")
    #print("Insurer C : ",InsurerC)
    
    INSURERD = re.findall("INSURER D :.*\n", input_string) # Number in the end is the NAIC number
    if(INSURERD == []):
        INSURERD = re.findall("INSURER\s*D:.*\n", text)    
    InsurerD = "".join(INSURERD)
    InsurerD = InsurerD.lstrip("INSURER D:")
    InsurerD = InsurerD.rstrip(" ")
    InsurerD = InsurerD.replace("\n","")
    InsurerD = InsurerD.replace("\t","")
    #print("Insurer D : ",InsurerD)
    
    INSURERE = re.findall("INSURER E :.*\n", input_string) # Number in the end is the NAIC number
    if(INSURERE == []):
        INSURERE = re.findall("INSURER\s*E:.*\n", text)    
    InsurerE = "".join(INSURERE)
    InsurerE = InsurerE.lstrip("INSURER E:")
    InsurerE = InsurerE.rstrip(" ")
    InsurerE = InsurerE.replace("\n","")
    InsurerE = InsurerE.replace("\t","")
    #print("Insurer E : ",InsurerE)
    
    INSURERF = re.findall("INSURER F :.*\n", input_string) # Number in the end is the NAIC number
    if(INSURERF == []):
        INSURERF = re.findall("INSURER\s*F:.*\n", text)    
    InsurerF = "".join(INSURERF)
    InsurerF = InsurerF.lstrip("INSURER F:")
    InsurerF = InsurerF.rstrip(" ")
    InsurerF = InsurerF.replace("\n","")
    InsurerF = InsurerF.replace("\t","")
    #print("Insurer F : ",InsurerF)
    
    #CGL
    cgl = re.findall("(?s)COMMERCIAL GENERAL LIABILITY.*?AUTOMOBILE LIABILITY", input_string)
    textcgl = re.findall("(?s)COMMERCIAL GENERAL LIABILITY.*?AUTOMOBILE LIABILITY", text)
    CGL = "".join(cgl)
    TEXTCGL = "".join(textcgl)
    #print(text)
    policyno = ""
    effdate = ""
    expdate = ""
    pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}/\d{1,2}/\d{4}",CGL)
    for policy in pol1:
        policy = policy.replace("\t"," ")
        policy = policy.lstrip(" ")
        if(policy != ""):
            policyno,effdate,expdate = policy.split(' ',3)
    
    cgl_policy_no = policyno
    cgl_eff_date = effdate
    cgl_exp_date = expdate
    
    if(cgl_policy_no == ""):
        policyno = ""
        effdate = ""
        expdate = ""
        pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}",TEXTCGL)
        policy = "".join(pol1)
        policy = policy.replace("\t"," ")
        policy = policy.lstrip(" ")
        policy = policy.replace("|","")
        if(policy != ""):
            policyno,effdate,expdate = policy.split()    
        cgl_policy_no = policyno
        cgl_eff_date = effdate
        cgl_exp_date = expdate
    #print("CGL Policy number : ",cgl_policy_no)
    #print("CGL Eff Date : ",cgl_eff_date)
    #print("CGL Exp Date : ",cgl_exp_date)
    
    #Limits
    EACHOCCURRENCE = re.findall("EACH OCCURRENCE\n*.*\d\n", CGL)
    if(EACHOCCURRENCE == []):
        EACHOCCURRENCE = re.findall("EACH OCCURRENCE\n*.*\d\n", text)
        if(EACHOCCURRENCE == []):
            eachoccurrence = ""
        else:
            eachoccurrence = "".join(EACHOCCURRENCE[0])
            eachoccurrence = eachoccurrence.lstrip("EACH OCCURRENCE")
            eachoccurrence = eachoccurrence.replace("\n","")
            eachoccurrence = eachoccurrence.replace("\t","")
    
    else:
        eachoccurrence = "".join(EACHOCCURRENCE[0])    
        eachoccurrence = eachoccurrence.lstrip("EACH OCCURRENCE")
        eachoccurrence = eachoccurrence.replace("\n","")
        eachoccurrence = eachoccurrence.replace("\t","")
    
    DAMAGETORENTED = re.findall("DAMAGE TO RENTED.*\d",CGL)
    if(DAMAGETORENTED == []):
        DAMAGETORENTED = re.findall("\(Ea occurrence\)\s*.*\d\n",CGL)
        if(DAMAGETORENTED == []):
            DAMAGETORENTED = re.findall("DAMAGE TO RENTED.*\d",text)
            if(DAMAGETORENTED == []):
                DAMAGETORENTED = re.findall("\(Ea occurrence\)\s*.*\d\n",text)
    damagetorented = "".join(DAMAGETORENTED)
    damagetorented = damagetorented.lstrip("DAMAGE TO RENTED")
    damagetorented = damagetorented.lstrip("(Ea occurrence)")
    damagetorented = damagetorented.lstrip("DAMAGE TO RENTED PREMISES (Ea occurrence)")
    damagetorented = damagetorented.replace("\t","")
    damagetorented = damagetorented.replace("|","")
    damagetorented = damagetorented.replace("_","")
    damagetorented = damagetorented.replace("\n","")
    
    MEDEXP = re.findall("MED EXP \(Any one person\)\s.\n*.*\d\n", CGL)
    if(MEDEXP == []):
        MEDEXP = re.findall("MED EXP \(Any one person\)\s.\n*.*\d\n", text)
    medexp = "".join(MEDEXP)
    medexp = medexp.lstrip("MED EXP (Any one person)")
    medexp = medexp.replace("\t","")
    medexp = medexp.replace("\n","")
    medexp = medexp.replace("_","")
    medexp = medexp.replace("|","")
    
    PERSONALADV = re.findall("PERSONAL & ADV INJURY\s*\$\s*\n*.*\d\n", CGL)
    if(PERSONALADV == []):
        PERSONALADV = re.findall("[Pp][Ee]RSONAL\s*&\s*ADV\s*INJURY\s*\s*\n*.*\d\n", text)
        personaladv = "".join(PERSONALADV)
        personalADV = re.sub("[Pp][Ee]RSONAL\s*&\s*ADV\s*INJURY","",personaladv)
        PERSONALADV = personalADV
        personaladv = ""
    personaladv = "".join(PERSONALADV)
    personaladv = personaladv.lstrip("PERSONAL & ADV INJURY")
    personaladv = personaladv.replace("\n","")
    personaladv = personaladv.replace("\t","")
    personaladv = personaladv.replace("_","")
    personaladv = personaladv.replace("|","")
    
    GENERALAGGREGATE = re.findall("GENERAL AGGREGATE\n*.*\d\n", CGL)
    if(GENERALAGGREGATE == []):
        GENERALAGGREGATE = re.findall("GENERAL AGGREGATE\n*.*\d\n", text)
    generalaggregate = "".join(GENERALAGGREGATE)
    generalaggregate = generalaggregate.lstrip("GENERAL AGGREGATE")
    generalaggregate = generalaggregate.replace("\n","")
    generalaggregate = generalaggregate.replace("\t","")
    generalaggregate = generalaggregate.replace("_","") 
    generalaggregate = generalaggregate.replace("|","")
    
    PRODUCTCOMP = re.findall("COMP/OP AGG\n*.*\d\n", CGL)
    if(PRODUCTCOMP == []):
        PRODUCTCOMP = re.findall("C[Oo][Mm]P/OP AGG\n*.*\d\n", text)
        productcomp = "".join(PRODUCTCOMP)
        ProductCOMP = re.sub("C[Oo][Mm]P/OP AGG","",productcomp)
        PRODUCTCOMP = ProductCOMP
        productcomp = ""
    productcomp = "".join(PRODUCTCOMP)
    productcomp = productcomp.lstrip("COMP/OP AGG")
    productcomp = productcomp.replace("\n","")
    productcomp = productcomp.replace("\t","")
    
    COMMGENLIAB = re.findall("X\s*COMMERCIAL GENERAL LIABILITY",input_string)
    if(COMMGENLIAB == []):
        COMMGENLIAB = re.findall("X \| COMMERCIAL GENERAL LIABILITY",text)
    commgenliab = "".join(COMMGENLIAB)
    commgenliab = commgenliab.rstrip(" COMMERCIAL GENERAL LIABILITY")
    commengenliab = commgenliab.replace("\n","")
    commengenliab = commgenliab.replace("\t","")
    commengenliab = commgenliab.replace("|","")
    
    CLAIMSMADE = re.findall("X CLAIMS-MADE",CGL)
    if(CLAIMSMADE == []):
        CLAIMSMADE = re.findall("X \| CLAIMS-MADE",text)
    claimsmade = "".join(CLAIMSMADE)
    claimsmade = claimsmade.rstrip(" CLAIMS-MADE")
    claimsmade = claimsmade.replace("\n","")
    claimsmade = claimsmade.replace("\t","")
    claimsmade = claimsmade.replace("|","")
    
    OCCUR = re.findall("X OCCUR",CGL)
    if(OCCUR == []):
        OCCUR = re.findall("X \| OCCUR",text)
    occur_cgl = "".join(OCCUR)
    occur_cgl = occur_cgl.rstrip(" OCCUR")
    occur_cgl = occur_cgl.replace("\n","")
    occur_cgl = occur_cgl.replace("\t","")
    occur_cgl = occur_cgl.replace("|","") 
    
    BLKTADDINS = re.findall("X Blkt Add'l Ins",CGL)
    if(BLKTADDINS == []):
        BLKTADDINS = re.findall("X \| Blkt Add'l Ins",text)
    blktaddins = "".join(BLKTADDINS)
    blktaddins =  blktaddins.rstrip(" Blkt Add'l Ins")
    blktaddins = blktaddins.replace("\n","")
    blktaddins = blktaddins.replace("\t","")
    blktaddins = blktaddins.replace("|","")
    
    BLKTWVR = re.findall("X Blkt Waiver",CGL)
    if(BLKTWVR == []):
        BLKTWVR = re.findall("X \| Blkt Waiver",text)
    blktwvr = "".join(BLKTWVR)
    blktwvr = blktwvr.rstrip(" Blkt Waiver")
    blktwvr = blktwvr.replace("\n","")
    blktwvr = blktwvr.replace("\t","")
    blktwvr = blktwvr.replace("|","")
    
    POLICY = re.findall("X POLICY",CGL)
    if(POLICY == []):
        POLICY = re.findall("X \| P",text)
    policy = "".join(POLICY)
    policy = policy.rstrip(" POLICY")
    policy = policy.replace("\n","")
    policy = policy.replace("\t","")
    policy = policy.replace("|","")
    
    PROJECT = re.findall("X PRO-JECT",CGL)
    if(PROJECT == []):
        PROJECT = re.findall("X \| PRO-JECT",text)
    project = "".join(PROJECT)
    project = project.rstrip(" PRO-JECT")
    project = project.replace("\n","")
    project = project.replace("\t","")
    project = project.replace("|","")
    
    LOC = re.findall("X LOC",CGL)
    if(LOC == []):
        LOC = re.findall("X \| LOC",text)
    loc = "".join(LOC)
    loc = loc.rstrip(" LOC")
    loc = loc.replace("\n","")
    loc = loc.replace("\t","")
    loc = loc.replace("|","")
    
    OTHER = re.findall("X OTHER",CGL)
    if(OTHER == []):
        OTHER = re.findall("X \| OTHER",text)
    other = "".join(OTHER)
    other = other.rstrip(" OTHER")
    other = other.replace("\n","")
    other = other.replace("\t","")
    other = other.replace("|","")
    
    #AML
    aml = re.findall("(?s)AUTOMOBILE LIABILITY.*?UMBRELLA LIAB",input_string)
    AML = "".join(aml)
    textaml = re.findall("(?s)AUTOMOBILE LIABILITY.*?UMBRELLA LIAB",text)
    TEXTAML = "".join(textaml)
    
    policyno = ""
    effdate = ""
    expdate = ""
    pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}/\d{1,2}/\d{4}", AML)
    for policy in pol1:
        policy = policy.replace("\t", " ")
        policy = policy.replace("\n", "")
        policy = policy.lstrip(" ")
        if (policy != ""):
            policyno, effdate, expdate = policy.split(' ', 3)

    AML_Policy_no = policyno
    AML_Eff_Date = effdate
    AML_Exp_Date = expdate
    if(AML_Policy_no == ""):
        policyno = ""
        effdate = ""
        expdate = ""
        pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}",TEXTAML)
        for policy in pol1:
            policy = policy.replace("\t"," ")
            policy = policy.lstrip(" ")
            policy = policy.replace("|","")
            if(policy != ""):
                policyno,effdate,expdate = policy.split()    
        AML_Policy_no = policyno
        AML_Eff_Date = effdate
        AML_Exp_Date = expdate
    
    #Limits
    CSLEA = re.findall("COMBINED SINGLE LIMIT.*\d", AML)
    if(CSLEA == []):
        CSLEA = re.findall("\(Ea accident\)\s.\n*.*\d\n", AML)
        if(CSLEA == []):
            CSLEA = re.findall("COMBINED SINGLE LIMIT.*\d", TEXTAML)
            if(CSLEA == []):
                CSLEA = re.findall("\(Ea accident\)\s.\n*.*\d\n", TEXTAML)
    
    cslea = "".join(CSLEA)
    cslea = cslea.lstrip("(Ea accident)")
    cslea = cslea.lstrip("COMBINED SINGLE LIMIT")
    cslea = cslea.lstrip("COMBINED SINGLE LIMIT(Ea accident)")
    cslea = cslea.replace("\t","")
    cslea = cslea.replace("\n","")
    
    BIP = re.findall("BODILY INJURY \(Per person\)\s.*\n",AML)
    if(BIP == []):
        BIP = re.findall("BODILY INJURY \(Per person\)\s.*\n",TEXTAML)
    bip = "".join(BIP)
    bip = bip.lstrip("BODILY INJURY (Per person)")
    bip = bip.replace("\t","")
    bip = bip.replace("\n","")
    
    BIA = re.findall("BODILY INJURY \(Per accident\)\s.*\n", AML)
    if(BIA == []):
        BIA = re.findall("BODILY INJURY \(Per accident\)\s.*\n", AML)
    bia = "".join(BIA)
    bia = bia.lstrip("BODILY INJURY (Per accident)")
    bia = bia.replace("\t","")
    bia = bia.replace("\n","")
    
    ANYAUTO = re.findall("X ANY AUTO",AML)
    if(ANYAUTO == []):
        ANYAUTO = re.findall("X \| ANY AUTO",text)
    anyauto = "".join(ANYAUTO)
    anyauto = anyauto.rstrip(" ANY AUTO")
    anyauto = anyauto.replace("\n","")
    anyauto = anyauto.replace("\t","")
    anyauto = anyauto.replace("|","")
    
    OWNED = re.findall("X OWNED",AML)
    if(OWNED == []):
        OWNED = re.findall("X \| OWNED",text)
    owned = "".join(OWNED)
    owned = owned.rstrip(" OWNED")
    owned = owned.replace("\n","")
    owned = owned.replace("\t","")
    owned = owned.replace("|","")
    
    SCHEDULED = re.findall("X SCHEDULED",AML)
    if(SCHEDULED == []):
        SCHEDULED = re.findall("X \| SCHEDULED",text)
    scheduled = "".join(SCHEDULED)
    scheduled = scheduled.rstrip(" SCHEDULED")
    scheduled = scheduled.replace("\n","")
    scheduled = scheduled.replace("\t","")
    scheduled = scheduled.replace("|","")
    
    HIRED = re.findall("X HIRED",AML)
    if(HIRED == []):
        HIRED = re.findall("X \| HIRED",text)
    hired = "".join(HIRED)
    hired = hired.rstrip(" HIRED")
    hired = hired.replace("\n","")
    hired = hired.replace("\t","")
    hired = hired.replace("|","")
    
    NONOWNED = re.findall("X NON-OWNED",AML)
    if(NONOWNED == []):
        NONOWNED = re.findall("X \| NON-OWNED",text)
    nonowned = "".join(NONOWNED)
    nonowned = nonowned.rstrip(" NON-OWNED")
    nonowned = nonowned.replace("\n","")
    nonowned = nonowned.replace("\t","")
    nonowned = nonowned.replace("|","")
    
    #UmbrellaLiab
    ulb = re.findall("(?s)UMBRELLA LIAB.*WORKERS COMPENSATION",input_string)
    ULB = "".join(ulb)
    ulbtext = re.findall("(?s)UMBRELLA LIAB.*WORKERS COMPENSATION", text)
    ULBTEXT = "".join(ulbtext)

    #Limits
    pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}/\d{1,2}/\d{4}",ULB)
    policyno = ""
    effdate = ""
    expdate = ""
    for policy in pol1:
        policy = policy.replace("\t"," ")
        policy = policy.replace("\n","")
        policy = policy.lstrip(" ")
        if(policy != ""):
            policyno,effdate,expdate = policy.split(' ',3)
            
    umb_policy_no = policyno
    umb_eff_date = effdate
    umb_exp_date = expdate
    
    if(umb_policy_no == ""):
        pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}",ULBTEXT)
        policyno = ""
        effdate = ""
        expdate = ""
        for policy in pol1:
            policy = policy.replace("\t"," ")
            policy = policy.replace("\n","")
            policy = policy.replace("|","")
            policy = policy.lstrip(" ")
            if(policy != ""):
                policyno,effdate,expdate = policy.split()
            
        umb_policy_no = policyno
        umb_eff_date = effdate
        umb_exp_date = expdate
    
    EACHOCCURRENCE = re.findall("EACH OCCURRENCE.*\n",ULB)
    if(EACHOCCURRENCE == []):
        EACHOCCURRENCE = re.findall("EACH OCCURRENCE.*\n",ULBTEXT)
    umb_each_occurrence = "".join(EACHOCCURRENCE)
    umb_each_occurrence = umb_each_occurrence.lstrip("EACH OCCURRENCE")
    umb_each_occurrence = umb_each_occurrence.replace("\t","")
    umb_each_occurrence = umb_each_occurrence.replace("|","")
    umb_each_occurrence = umb_each_occurrence.replace("\n","")
    
    AGGREGATE = re.findall("AGGREGATE.*\n",ULB)
    if(AGGREGATE == []):
        AGGREGATE = re.findall("AGGREGATE.*\n",ULBTEXT)
    aggregate = "".join(AGGREGATE)
    aggregate = aggregate.lstrip("AGGREGATE")
    aggregate = aggregate.replace("\t","")
    aggregate = aggregate.replace("\n","")
    aggregate = aggregate.replace("|","")
    
    UMBRELLALIAB = re.findall("X UMBRELLA LIAB",input_string)
    if(UMBRELLALIAB == []):
        UMBRELLALIAB = re.findall("X \| UMBRELLA LIAB",text)
    umbrellaliab = "".join(UMBRELLALIAB)
    umbrellaliab = umbrellaliab.rstrip(" UMBRELLA LIAB")
    umbrellaliab = umbrellaliab.replace("\t","")
    umbrellaliab = umbrellaliab.replace("\n","")
    
    OCCUR = re.findall("X OCCUR",ULB)
    if(OCCUR == []):
        OCCUR = re.findall("X \| OCCUR",ULBTEXT)
    umb_occur = "".join(OCCUR)
    umb_occur = umb_occur.rstrip(" OCCUR")
    umb_occur = umb_occur.replace("\t","")
    umb_occur = umb_occur.replace("\n","")
    
    EXCESSLIAB = re.findall("X EXCESS LIAB",ULB)
    if(EXCESSLIAB == []):
        EXCESSLIAB = re.findall("X \| EXCESS LIAB",text)
    excessliab = "".join(EXCESSLIAB)
    excessliab = excessliab.rstrip(" EXCESS LIAB")
    excessliab = excessliab.replace("\t","")
    excessliab = excessliab.replace("\n","")
    
    CLAIMSMADE = re.findall("X CLAIMS-MADE",ULB)
    if(CLAIMSMADE == []):
        CLAIMSMADE = re.findall("X \| CLAIMS-MADE",ULBTEXT)
    umb_claimsmade = "".join(CLAIMSMADE)
    umb_claimsmade = umb_claimsmade.rstrip(" CLAIMS-MADE")
    umb_claimsmade = umb_claimsmade.replace("\t","")
    umb_claimsmade = umb_claimsmade.replace("\n","")
    
    #Workers
    wc = re.findall("(?s)WORKERS COMPENSATION.*?Additional Remarks",input_string)
    WC = "".join(wc)
    wctext = re.findall("(?s)WORKERS COMPENSATION.*?Additional Remarks",text)
    WCTEXT = "".join(wctext)

    policyno = ""
    effdate = ""
    expdate = ""
    pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}/\d{1,2}/\d{4}",WC)
    for policy in pol1:
        policy = policy.replace("\t"," ")
        policy = policy.replace("\n","")
        policy = policy.lstrip(" ")
        if(policy != ""):
            policyno,effdate,expdate = policy.split(' ',3)

    wc_policy_no = policyno
    wc_eff_date = effdate
    wc_exp_date = expdate
    
    if(wc_policy_no == []):
        policyno = ""
        effdate = ""
        expdate = ""
        pol1 = re.findall("\s[A-Z0-9'.'-]+\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}\s*\|*\s*\d{1,2}/\d{1,2}/\d{4}",WCTEXT)
        for policy in pol1:
            policy = policy.replace("\t"," ")
            policy = policy.replace("\n","")
            policy = policy.replace("|","")
            policy = policy.lstrip(" ")
            if(policy != ""):
                policyno,effdate,expdate = policy.split()
        wc_policy_no = policyno
        wc_eff_date = effdate
        wc_exp_date = expdate
    
    ELA = re.findall("E.L. EACH ACCIDENT.*\n", WC)
    if(ELA == []):
        ELA = re.findall("E.L. EACH ACCIDENT.*\n", WCTEXT)
    ela = "".join(ELA)
    ela = ela.lstrip("E.L. EACH ACCIDENT ")
    ela = ela.replace("\t","")
    ela = ela.replace("|","")
    ela = ela.replace("\n","")
    
    ELD = re.findall("E.L. DISEASE - EA EMPLOYEE.*\d",WC)
    if(ELD == []):
        ELD = re.findall("E.L. DISEASE - EA EMPLOYEE.*\d",WCTEXT)
    eld = "".join(ELD)
    eld = eld.lstrip("E.L. DISEASE - EA EMPLOYEE ")
    eld = eld.replace("\t","")
    eld = eld.replace("|","")
    eld = eld.replace("\n","")
    
    ELDPL = re.findall("E.L. DISEASE - POLICY LIMIT.*\d",WC)
    if(ELDPL == []):
        ELDPL = re.findall("E.L. DISEASE - POLICY LIMIT.*\d",WCTEXT)
    eldpl = "".join(ELDPL)
    eldpl = eldpl.lstrip("E.L. DISEASE - POLICY LIMIT ")
    eldpl = eldpl.replace("\t","")
    eldpl = eldpl.replace("|","")
    eldpl = eldpl.replace("\n","")
    
    EXCLUDEDYN = re.findall("EXCLUDED\?\,* [N,Y]",WC)
    if(EXCLUDEDYN == []):
        EXCLUDEDYN = re.findall("EXCLUDED\?\,* [N,Y]",text)
    excludeyn = "".join(EXCLUDEDYN)
    excludeyn = excludeyn.lstrip("EXCLUDED?")
    excludeyn = excludeyn.replace("\t","")
    excludeyn = excludeyn.replace(",","")
    excludeyn = excludeyn.replace("|","")
    excludeyn = excludeyn.replace("\n","")
    
    DOLV_Reg_ex = ["DESCRIPTION OF OPERATIONS / LOCATIONS / VEHICLES\s*\(Attach ACORD 101, Additional Remarks Schedule, if more space is required\)\n.*","DESCRIPTION OF OPERATIONS\s*/\s*LOCATIONS\s*/\s*VEHICLES\s*\(ACORD 101, Additional Remarks Schedule, may be attached if more space is required\)\n.*"]
    for reg in DOLV_Reg_ex:
        DOLV = re.findall(reg,input_string)
        dolv = "".join(DOLV)
        dolv = dolv.lstrip("DESCRIPTION OF OPERATIONS / LOCATIONS / VEHICLES  (ACORD 101, Additional Remarks Schedule, may be attached if more space is required)")
        dolv = dolv.replace("\t","")
        dolv = dolv.replace("\n","")
    if(DOLV == []):
        DOLV = re.findall("DESCRIPTION OF OPERATIONS / LOCATIONS / VEHICLES \(ACORD 101, Additional Remarks Schedule, may be attached if more space is required\)\n.*",text)
        dolv = "".join(DOLV)
        dolv = dolv.lstrip("DESCRIPTION OF OPERATIONS / LOCATIONS / VEHICLES  (ACORD 101, Additional Remarks Schedule, may be attached if more space is required)")
        dolv = dolv.replace("\t","")
        dolv = dolv.replace("\n","")

    cn = re.findall("CERTIFICATE NUMBER:.*REVISION NUMBER", text)
    CN = "".join(cn)
    CN = CN.replace("CERTIFICATE NUMBER:", "")
    CN = CN.replace("REVISION NUMBER", "")
    CN = CN.replace("\t", "")

    rn = re.findall("REVISION NUMBER:.*", text)
    RN = "".join(rn)
    RN = RN.replace("REVISION NUMBER:", "")
    RN = RN.replace("\t", "")

    
    ch = re.findall("(?s)\nCERTIFICATE HOLDER.*\s[A-Z]{2}\s*\d{5}\s", text)
    if (ch == []):
        ch = re.findall("(?s)NOTICE WILL BE DELIVERED IN.*\s[A-Z]{2}\s*\d{5}\s", text)
    CH = "".join(ch)
    CH = CH.replace("\n", "")
    CH = CH.replace("ACCORDANCE WITH THE POLICY PROVISIONS", "")
    CH = CH.replace("NOTICE WILL BE DELIVERED IN", "")
    CH = CH.replace("\t", "")
    CH = CH.replace("CERTIFICATE HOLDER", "")
    CH = CH.replace("CANCELLATION", "")
    #print(CH)

    info.update({file: {'Date': Date, 'Producer': prod_Insured_Address, 'Insured': ins_Insured_Address, 'Name': Name,
                        'Email': Email, 'Insurer A': InsurerA, 'Insurer B': InsurerB, 'Insurer C': InsurerC,
                        'Insurer D': InsurerD, 'Insurer E': InsurerE, 'Insurer F': InsurerF,
                        'COMMERCIAL GENERAL LIABILITY': {'Commercial general liability': commgenliab,
                                                         'Claims made': claimsmade, 'Occur': occur_cgl,
                                                         'BlktAddins': blktaddins, 'BlktWvr': blktwvr,
                                                         'Project': project, 'LOC': loc, 'Other': other,
                                                         'Policy number': cgl_policy_no, 'Eff Date': cgl_eff_date,
                                                         'Exp Date': cgl_exp_date, 'Each occurrence': eachoccurrence,
                                                         'Damage to rented': damagetorented, 'Med Exp': medexp,
                                                         'Personal Adv': personaladv,
                                                         'General Aggregate': generalaggregate,
                                                         'Product Comp': productcomp},
                        'AUTOMOBILE LIABILITY': {'Any Auto': anyauto, 'Owned': owned, 'Scheduled': scheduled,
                                                 'Hired': hired, 'Non Owned': nonowned, 'Policy number': AML_Policy_no,
                                                 'Eff Date': AML_Eff_Date, 'Exp Date': AML_Exp_Date,
                                                 'Combined Single Limit': cslea, 'Bodily Injury (per person)': bip,
                                                 'Bodily Injury (per accident)': bia},
                        'Umbrella Liability': {'Umbrella Liab': umbrellaliab, 'Occur': umb_occur,
                                               'Excess Liab': excessliab, 'Claims made': umb_claimsmade,
                                               'Policy number': umb_policy_no, 'Eff Date': umb_eff_date,
                                               'Exp Date': umb_exp_date, 'Each occurrence': umb_each_occurrence,
                                               'Aggregate': aggregate},
                        'Workers Compensation': {'ANY PROPRIETOR/PARTNER/EXECUTIVE OFFICER/MEMBER EXCLUDED?': excludeyn,
                                                 'Policy number': wc_policy_no, 'Eff Date': wc_eff_date,
                                                 'Exp Date': wc_exp_date, 'E.L Each Accident': ela,
                                                 'E.L. DISEASE - EA EMPLOYEE': eld,
                                                 'E.L. DISEASE - POLICY LIMIT': eldpl},
                        'Description of operations / locations / vehicles': dolv,
                        'Certificate number': CN, 'Revision number': RN, 'Certificate Holder': CH
                        }
                 })

    #print(info)
    return info,input_string