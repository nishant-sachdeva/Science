dna_to_rna = {
    'a' : 'u' ,  
    't' : 'a' ,  
    'g' : 'c' ,  
    'c' : 'g' ,  
}


rna_to_protein = {
    'uuu' : 'phe',
    'uuc' : 'phe',
    'uua' : 'Leu',
    'uug' : 'Leu',

    'ucu' : 'Ser',
    'ucc' : 'Ser',
    'uca' : 'Ser',
    'ucg' : 'Ser',

    'uac' : 'tyr',
    'uau' : 'tyr',
    'uaa' : 'STOP\n',
    'uag' : 'STOP\n',

    'ugu' : 'cys',
    'ugc' : 'cys',
    'uga' : 'STOP\n',
    'ugg' : 'trp',

    'cuu' : 'leu',
    'cuc' : 'leu',
    'cua' : 'leu',
    'cug' : 'leu',

    'ccu' : 'pro',
    'ccc' : 'pro',
    'cca' : 'pro',
    'ccg' : 'pro',

    'cau' : 'his',
    'cac' : 'his',
    'caa' : 'gln',
    'cag' : 'gln',

    'cgu' : 'arg',
    'cgc' : 'arg',
    'cga' : 'arg',
    'cgg' : 'arg',

    'auu' : 'ile',
    'auc' : 'ile',
    'aua' : 'ile',
    'aug' : 'met',


    'acu' : 'thr',
    'acc' : 'thr',
    'aca' : 'thr',
    'acg' : 'thr',


    'aau' : 'asn',
    'aac' : 'asn',
    'aaa' : 'lys',
    'aag' : 'lys',


    'agu' : 'ser',
    'agc' : 'ser',
    'aga' : 'arg',
    'agg' : 'arg',


    'guu' : 'val',
    'guc' : 'val',
    'gua' : 'val',
    'gug' : 'val',


    'gcu' : 'ala',
    'gcc' : 'ala',
    'gca' : 'ala',
    'gcg' : 'ala',


    'gau' : 'asp',
    'gac' : 'asp',
    'gaa' : 'glu',
    'gag' : 'glu',


    'ggu' : 'gly',
    'ggc' : 'gly',
    'gga' : 'gly',
    'ggg' : 'gly',
}