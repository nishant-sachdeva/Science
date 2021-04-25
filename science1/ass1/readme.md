Instructions for running the code :

python3 ques1.py << path for the file containing the dna sequence >>

Requirements :

1. re
2. python3


Points to note : 
1. It is  assumed that the given DNA is one side of the Double Helix structure. For converting to RNA, we practically have to merely swap 'T' with 'U' . 
2. For conversion of RNA to Proteins. Find all the 'aug' sites, and then make the longest Polypeptide that you can. For the given sample DNA the proteins that can be made are : 

1  :  met-STOP

2  :  met-lys-pro-val-asp-Leu-val-thr-ala-STOP

3  :  met-tyr-leu-thr-pro-leu-gln-thr-gly-phe-ala-glu-asn-ile-trp-val-his-Ser-arg-val-met-Ser-lys-gln-val-ile-pro-ala-lys-asn-asn-STOP

4  :  met-Ser-lys-gln-val-ile-pro-ala-lys-asn-asn-STOP

5  :  met-met-Ser-arg-leu-gln-glu-pro-asn-tyr-pro-val-arg-arg-Ser-asn-ser-Ser-gln-arg-STOP

6  :  met-Ser-arg-leu-gln-glu-pro-asn-tyr-pro-val-arg-arg-Ser-asn-ser-Ser-gln-arg-STOP

7  :  met-val-pro-STOP